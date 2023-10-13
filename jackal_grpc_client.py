# modified from: VisionRobot/src/vision/client.py

import abc
import jwt
import sys
import grpc
import asyncio
import logging
import argparse
import datetime
from vision_grpc.vision_grpc import auth_pb2_grpc
from vision_grpc.vision_grpc import serve_pb2_grpc
from vision_grpc.vision_grpc import manage_pb2_grpc
from vision_grpc.vision_grpc import manage_pb2  # noqa: F401
from vision_grpc.vision_grpc import message_pb2  # noqa: F401
from google.protobuf import text_format  # noqa: F401
from google.protobuf import wrappers_pb2  # noqa: F401
from google.protobuf import timestamp_pb2  # noqa: F401
from google.protobuf import duration_pb2  # noqa: F401
from google.protobuf import empty_pb2  # noqa: F401
from google.protobuf import any_pb2  # noqa: F401
from google.protobuf import json_format


class UnaryUnaryClientCallDetailsInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self, function):
        self.function = function

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        return await continuation(self.function(client_call_details), request)


class UnaryStreamClientCallDetailsInterceptor(grpc.aio.UnaryStreamClientInterceptor):
    def __init__(self, function):
        self.function = function

    async def intercept_unary_stream(self, continuation, client_call_details, request):
        return await continuation(self.function(client_call_details), request)


class StreamUnaryClientCallDetailsInterceptor(grpc.aio.StreamUnaryClientInterceptor):
    def __init__(self, function):
        self.function = function

    async def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        return await continuation(self.function(client_call_details), request_iterator)


class ClientCallDetailsCallable(abc.ABC):
    @abc.abstractmethod
    def __call__(self, client_call_details):
        raise NotImplementedError("__callback__")


class LoggingClientCallDetails(ClientCallDetailsCallable):
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, client_call_details):
        self.logger.info(
            f">{client_call_details.method.decode()} {client_call_details}"
        )
        return client_call_details


class ClientMetadata(ClientCallDetailsCallable):
    def __init__(self, metadata):
        self.metadata = metadata

    def __call__(self, client_call_details):
        metadata = list(
            [] if client_call_details.metadata is None else client_call_details.metadata
        ) + list(self.metadata)
        return grpc.aio.ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
            client_call_details.wait_for_ready,
        )


class ClientLogger(abc.ABC):
    def __init__(self, logger, direction, level):
        self.logger = logger
        self.direction = direction
        self.level = level

    @abc.abstractmethod
    def function(self, message):
        raise

    def __call__(self, method, message):
        if self.logger.isEnabledFor(self.level):
            string = self.function(message)
            #self.logger.info(f"{self.direction}{method} {string}")


class ClientMessageLogger(ClientLogger, abc.ABC):
    def __init__(self, logger, direction, level):
        super().__init__(logger, direction, level)

    def function(self, message):
        return text_format.MessageToString(message, as_one_line=True)


class ClientRequestLogger(ClientMessageLogger):
    def __init__(self, logger):
        super().__init__(logger, ">", logging.DEBUG)


class ClientResponseLogger(ClientMessageLogger):
    def __init__(self, logger):
        super().__init__(logger, "<", logging.DEBUG)


class AuthChannel:
    def __init__(self, grpc_address):
        self.grpc_address = grpc_address

    def __call__(self):
        if ":" in self.grpc_address:
            return grpc.aio.insecure_channel(
                self.grpc_address,
                interceptors=[
                    UnaryUnaryClientCallDetailsInterceptor(
                        LoggingClientCallDetails(logging.getLogger())
                    ),
                ],
            )
        return grpc.aio.secure_channel(
            self.grpc_address,
            grpc.ssl_channel_credentials(),
            interceptors=[
                UnaryUnaryClientCallDetailsInterceptor(
                    LoggingClientCallDetails(logging.getLogger())
                ),
            ],
        )


class ServeChannel:
    def __init__(self, grpc_address, user, jwt_secret):
        self.grpc_address = grpc_address
        sub = user
        exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(
            weeks=1
        )
        access_token = jwt.encode(
            {
                "sub": sub,
                "exp": exp,
            },
            jwt_secret,
        )
        self.authorization = f"Bearer {access_token}"

    def __call__(self, device):
        if ":" in self.grpc_address:
            return grpc.aio.insecure_channel(
                self.grpc_address,
                interceptors=[
                    StreamUnaryClientCallDetailsInterceptor(
                        ClientMetadata(
                            [
                                ("device", device),
                                ("authorization", self.authorization),
                            ]
                        )
                    ),
                    StreamUnaryClientCallDetailsInterceptor(
                        LoggingClientCallDetails(logging.getLogger())
                    ),
                    UnaryStreamClientCallDetailsInterceptor(
                        ClientMetadata(
                            [
                                ("device", device),
                                ("authorization", self.authorization),
                            ]
                        )
                    ),
                    UnaryStreamClientCallDetailsInterceptor(
                        LoggingClientCallDetails(logging.getLogger())
                    ),
                ],
            )
        return grpc.aio.secure_channel(
            self.grpc_address,
            grpc.ssl_channel_credentials(),
            interceptors=[
                StreamUnaryClientCallDetailsInterceptor(
                    ClientMetadata(
                        [
                            ("device", device),
                            ("authorization", self.authorization),
                        ]
                    )
                ),
                StreamUnaryClientCallDetailsInterceptor(
                    LoggingClientCallDetails(logging.getLogger())
                ),
                UnaryStreamClientCallDetailsInterceptor(
                    ClientMetadata(
                        [
                            ("device", device),
                            ("authorization", self.authorization),
                        ]
                    )
                ),
                UnaryStreamClientCallDetailsInterceptor(
                    LoggingClientCallDetails(logging.getLogger())
                ),
            ],
        )


class ManageChannel:
    def __init__(self, grpc_address, user, jwt_secret):
        self.grpc_address = grpc_address
        sub = user
        exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(
            weeks=1
        )
        access_token = jwt.encode(
            {
                "sub": sub,
                "exp": exp,
            },
            jwt_secret,
        )
        self.authorization = f"Bearer {access_token}"

    def __call__(self):
        if ":" in self.grpc_address:
            return grpc.aio.insecure_channel(
                self.grpc_address,
                interceptors=[
                    UnaryUnaryClientCallDetailsInterceptor(
                        ClientMetadata(
                            [
                                ("authorization", self.authorization),
                            ]
                        )
                    ),
                    UnaryUnaryClientCallDetailsInterceptor(
                        LoggingClientCallDetails(logging.getLogger())
                    ),
                ],
            )
        return grpc.aio.secure_channel(
            self.grpc_address,
            grpc.ssl_channel_credentials(),
            interceptors=[
                UnaryUnaryClientCallDetailsInterceptor(
                    ClientMetadata(
                        [
                            ("authorization", self.authorization),
                        ]
                    )
                ),
                UnaryUnaryClientCallDetailsInterceptor(
                    LoggingClientCallDetails(logging.getLogger())
                ),
            ],
        )


class AuthToken:
    def __init__(self, channel):
        self.channel = channel

    async def __call__(self, authorization):
        request = empty_pb2.Empty()
        ClientRequestLogger(logging.getLogger())("/Auth/Token", request)
        response = await auth_pb2_grpc.AuthStub(self.channel).Token(
            request, metadata=[("authorization", authorization)]
        )
        ClientResponseLogger(logging.getLogger())("/Auth/Token", response)
        return response


class SendTask:
    def __init__(self, channel, function, response_class):
        self.channel = channel
        self.function = function
        self.response_class = response_class

    async def __call__(self, message):
        request = any_pb2.Any()
        request.Pack(message)
        ClientRequestLogger(logging.getLogger())("/Serve/SendTask", request)
        response = await serve_pb2_grpc.ServeStub(self.channel).SendTask(
            iter([request]), metadata=[("function", self.function)]
        )
        ClientResponseLogger(logging.getLogger())("/Serve/SendTask", response)
        message = self.response_class()
        response.Unpack(message)
        return message


class RecvPost:
    def __init__(self, channel, function, response_class):
        self.channel = channel
        self.function = function
        self.response_class = response_class

    async def __call__(self, total):
        index = 0
        request = any_pb2.Any()
        request.Pack(empty_pb2.Empty())
        ClientRequestLogger(logging.getLogger())("/Serve/RecvPost", request)
        async for response in serve_pb2_grpc.ServeStub(self.channel).RecvPost(
            request, metadata=[("function", self.function)]
        ):
            ClientResponseLogger(logging.getLogger())("/Serve/RecvPost", response)
            message = self.response_class()
            response.Unpack(message)
            yield message
            index += 1
            if total > 0 and index >= total:
                break


class ManageMethod:
    def __init__(self, channel):
        self.channel = channel

    async def __call__(self, function, request):
        method = f"/Manage/{function}"
        ClientRequestLogger(logging.getLogger())(method, request)
        stub = manage_pb2_grpc.ManageStub(self.channel)
        call = getattr(stub, function)
        response = await call(request)
        ClientResponseLogger(logging.getLogger())(method, response)
        return response


def message_class(name):
    if name == "Empty":
        module = sys.modules["google.protobuf.empty_pb2"]
    elif name == "Duration":
        module = sys.modules["google.protobuf.duration_pb2"]
    elif name == "Timestamp":
        module = sys.modules["google.protobuf.timestamp_pb2"]
    else:
        module = message_pb2
    return getattr(module, name)


def manage_class(name):
    module = sys.modules["google.protobuf.empty_pb2"] if name == "Empty" else manage_pb2
    return getattr(module, name)


async def token(channel, args):
    authorization = args[0]
    token = await AuthToken(channel)(authorization)


async def post(channel, function, args, total=0):
    function = "none:Timestamp" if function is None else function
    function, function_response = tuple(function.split(":"))
    match function:
        case "none":
            pass
        case "temperature":
            pass
        case "navsat":
            pass
        case "pose":
            pass
        case "echo":
            pass
        case "map":
            pass
        case other:
            raise ValueError("invalid function class: ", other)

    msg_ret=None
    response_class = message_class(function_response)
    async for mymsg in RecvPost(channel, function, response_class)(total):
        print('mymsg ', type(mymsg))
        msg_ret = mymsg
        pass
    return msg_ret


async def task(channel, function, args, total=0):
    function = "echo:Timestamp:Empty" if function is None else function
    function, function_request, function_response = tuple(function.split(":"))
    match function:
        case "joy":
            pass
        case "goal":
            pass
        case "echo":
            pass
        case other:
            raise ValueError("invalid function class: ", other)

    request_class = message_class(function_request)
    message = request_class()

    if function == "joy":
        print(args[0])
        message = json_format.Parse(args[0], message)
    elif function == "goal":
        print(args[0])
        message = json_format.Parse(args[0], message)
    elif function == "echo":
        message.GetCurrentTime()

    response_class = message_class(function_response)
    message = await SendTask(channel, function, response_class)(message)


async def manage(channel, function, args):
    match function:
        case "AddDevice":
            pass
        case "DelDevice":
            pass
        case "ChangeDevice":
            pass
        case "AddLandmark":
            pass
        case "DelLandmark":
            pass
        case "ChangeLandmark":
            pass
        case "ListLandmark":
            pass
        case "ListDevice":
            pass
        case "ListUser":
            pass
        case "ChangeRole":
            pass
        case "Role":
            pass
        case other:
            raise ValueError("invalid function class: ", other)

    request_class = manage_class(f"{function}Request")
    request = request_class()
    print(args[0])
    request = json_format.Parse(args[0], request)
    response = await ManageMethod(channel)(function, request)


async def run_auth(grpc_address, args, call):
    async with AuthChannel(grpc_address)() as channel:
        await call(channel, args)


async def run_serve(grpc_address, device, function, user, jwt_secret, args, call, total=0):
    async with ServeChannel(grpc_address, user, jwt_secret)(device) as channel:
        msg_ret = await call(channel, function, args, total)
    return msg_ret


async def run_manage(grpc_address, device, function, user, jwt_secret, args, call):
    async with ManageChannel(grpc_address, user, jwt_secret)() as channel:
        await manage(channel, function, args)

def main_post(grpc="robot.coldspringworks.com", device="649dcfba-4dbf-11e6-9c43-bc0000c00000", 
        function="temperature:Temperature", 
        user="github:6932348", jwt_secret="123456"):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format="%(levelname).1s [%(asctime)s] [%(filename)20s:%(lineno)3s]: %(message)s",
    )
    #channel=ServeChannel(grpc, user, jwt_secret)(device)
    #run=post(channel, function, args=None)
    run=run_serve(grpc, device, function, user, jwt_secret, args=None, call=post, total=1)
    msg_ret = asyncio.run(run)
    print('msg_ret type: ', type(msg_ret))
    return msg_ret

def main(args=None):
    print('---args---: ' , args, sys.argv)
    parser = argparse.ArgumentParser()

    parser.add_argument("--grpc", dest="grpc", default="robot.coldspringworks.com")
    #parser.add_argument("--grpc", dest="grpc", default="127.0.0.1:50001")
    parser.add_argument(
#        "--device", dest="device", default="123e4567-e89b-12d3-a456-426614174000"
        "--device", dest="device", default="649dcfba-4dbf-11e6-9c43-bc0000c00000"
    )
    parser.add_argument("--function", dest="function", default=None)
    parser.add_argument("--user", dest="user", default="github:6932348")
    parser.add_argument("--jwt_secret", dest="jwt_secret", default=None)
    parser.add_argument("type", type=str)
    parser.add_argument("args", nargs=argparse.REMAINDER)

    args = parser.parse_args()
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format="%(levelname).1s [%(asctime)s] [%(filename)20s:%(lineno)3s]: %(message)s",
    )

#    logging.getLogger().info(f"{args}")

    match args.type:
        case "token":
            run = run_auth(args.grpc, args.args, token)
        case "post":
            run = run_serve(
                args.grpc,
                args.device,
                args.function,
                args.user,
                args.jwt_secret,
                args.args,
                post,
            )
        case "task":
            run = run_serve(
                args.grpc,
                args.device,
                args.function,
                args.user,
                args.jwt_secret,
                args.args,
                task,
            )
        case "manage":
            run = run_manage(
                args.grpc,
                args.device,
                args.function,
                args.user,
                args.jwt_secret,
                args.args,
                post,
            )
        case other:
            raise ValueError("invalid type: ", other)
    asyncio.run(run)


if __name__ == "__main__":
    main()
