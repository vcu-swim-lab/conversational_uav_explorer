from vision_grpc import serve_pb2_grpc
from vision_grpc import message_pb2
from google.protobuf import text_format
from google.protobuf import empty_pb2
from google.protobuf import any_pb2

import abc
import grpc
import json
import uuid


class UnaryUnaryClientCallDetailsInterceptor(grpc.UnaryUnaryClientInterceptor):
    def __init__(self, function):
        self.function = function

    def intercept_unary_unary(self, continuation, client_call_details, request):
        return continuation(self.function(client_call_details), request)


class UnaryStreamClientCallDetailsInterceptor(grpc.UnaryStreamClientInterceptor):
    def __init__(self, function):
        self.function = function

    def intercept_unary_stream(self, continuation, client_call_details, request):
        return continuation(self.function(client_call_details), request)


class StreamUnaryClientCallDetailsInterceptor(grpc.StreamUnaryClientInterceptor):
    def __init__(self, function):
        self.function = function

    def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        return continuation(self.function(client_call_details), request_iterator)


class ClientCallDetailsCallable(abc.ABC):
    @abc.abstractmethod
    def __call__(self, client_call_details):
        raise NotImplementedError("__call__")


class ClientMetadata(ClientCallDetailsCallable):
    def __init__(self, metadata):
        self.metadata = metadata

    def __call__(self, client_call_details):
        metadata = list(
            [] if client_call_details.metadata is None else client_call_details.metadata
        ) + list(self.metadata)
        details = grpc.ClientCallDetails()
        details.method = client_call_details.method
        details.timeout = client_call_details.timeout
        details.metadata = metadata
        details.credentials = client_call_details.credentials
        details.wait_for_ready = client_call_details.wait_for_ready
        details.compression = client_call_details.compression
        return details


class LoggingClientCallDetails(ClientCallDetailsCallable):
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, client_call_details):
        self.logger.info(f">{client_call_details.method} {client_call_details}")
        return client_call_details


class GRPCNode(abc.ABC):
    def __init__(self):
        super().__init__()

    def grpc_channel(self, interceptor_class):
        json_config = json.dumps(
            {
                "methodConfig": [
                    {
                        "name": [{"service": "Serve"}],
                        "retryPolicy": {
                            "maxAttempts": 5,
                            "initialBackoff": "1s",
                            "maxBackoff": "10s",
                            "backoffMultiplier": 2,
                            "retryableStatusCodes": ["UNAVAILABLE"],
                        },
                    }
                ]
            }
        )
        if ":" in self.grpc:
            channel = grpc.insecure_channel(
                self.grpc,
                options=[("grpc.service_config", json_config)],
            )
        else:
            channel = grpc.secure_channel(
                self.grpc,
                grpc.ssl_channel_credentials(),
                options=[("grpc.service_config", json_config)],
            )
        return grpc.intercept_channel(
            channel,
            interceptor_class(
                ClientMetadata(
                    [
                        ("device", self.device),
                    ]
                )
            ),
            interceptor_class(LoggingClientCallDetails(self.logger)),
        )

    def grpc_post(self, message):
        try:
            post = any_pb2.Any()
            post.Pack(message)
            self.logger.info(f">/Serve/SendPost {post}")
            if self.channel is None:
                self.channel = self.grpc_channel(
                    StreamUnaryClientCallDetailsInterceptor
                )
            stub = serve_pb2_grpc.ServeStub(self.channel)
            response = stub.SendPost(
                iter([post]),
                metadata=[
                    ("function", self.function),
                ],
            )
            self.logger.info(f"</Serve/SendPost {response}")
        except Exception as e:
            self.logger.info(f"</Serve/SendPost {e}")
            self.channel.close() if self.channel is not None else None
            self.channel = None

    def grpc_loop(self, function_class, function_call):
        try:
            request = any_pb2.Any()
            request.Pack(empty_pb2.Empty())
            self.logger.info(f">/Serve/RecvTask {request}")
            if self.channel is None:
                self.channel = self.grpc_channel(
                    UnaryStreamClientCallDetailsInterceptor
                )
            stub = serve_pb2_grpc.ServeStub(self.channel)
            for response in stub.RecvTask(
                request, timeout=5.0,
                metadata=[("function", self.function)],
            ):
                self.logger.info(f"</Serve/RecvTask {response}")
                task = function_class()
                response.Unpack(task)
                function_call(task)
        except grpc.RpcError as status:
            self.logger.info(f"{status}")
            self.channel.close() if self.channel is not None else None
            self.channel = None
