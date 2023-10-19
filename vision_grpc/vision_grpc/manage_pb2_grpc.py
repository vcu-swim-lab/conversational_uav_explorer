# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vision_grpc.vision_grpc import manage_pb2 as vision__grpc_dot_vision__grpc_dot_manage__pb2


class ManageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddDevice = channel.unary_unary(
                '/Manage/AddDevice',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddDeviceRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddDeviceResponse.FromString,
                )
        self.DelDevice = channel.unary_unary(
                '/Manage/DelDevice',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelDeviceRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelDeviceResponse.FromString,
                )
        self.ChangeDevice = channel.unary_unary(
                '/Manage/ChangeDevice',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeDeviceRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeDeviceResponse.FromString,
                )
        self.AddLandmark = channel.unary_unary(
                '/Manage/AddLandmark',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddLandmarkRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddLandmarkResponse.FromString,
                )
        self.DelLandmark = channel.unary_unary(
                '/Manage/DelLandmark',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelLandmarkRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelLandmarkResponse.FromString,
                )
        self.ChangeLandmark = channel.unary_unary(
                '/Manage/ChangeLandmark',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeLandmarkRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeLandmarkResponse.FromString,
                )
        self.ListLandmark = channel.unary_unary(
                '/Manage/ListLandmark',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListLandmarkRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListLandmarkResponse.FromString,
                )
        self.ListDevice = channel.unary_unary(
                '/Manage/ListDevice',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListDeviceRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListDeviceResponse.FromString,
                )
        self.ListUser = channel.unary_unary(
                '/Manage/ListUser',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListUserRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListUserResponse.FromString,
                )
        self.ChangeRole = channel.unary_unary(
                '/Manage/ChangeRole',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeRoleRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeRoleResponse.FromString,
                )
        self.Role = channel.unary_unary(
                '/Manage/Role',
                request_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.RoleRequest.SerializeToString,
                response_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.RoleResponse.FromString,
                )


class ManageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddLandmark(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelLandmark(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeLandmark(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListLandmark(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Role(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDevice,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddDeviceRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddDeviceResponse.SerializeToString,
            ),
            'DelDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.DelDevice,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelDeviceRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelDeviceResponse.SerializeToString,
            ),
            'ChangeDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeDevice,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeDeviceRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeDeviceResponse.SerializeToString,
            ),
            'AddLandmark': grpc.unary_unary_rpc_method_handler(
                    servicer.AddLandmark,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddLandmarkRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.AddLandmarkResponse.SerializeToString,
            ),
            'DelLandmark': grpc.unary_unary_rpc_method_handler(
                    servicer.DelLandmark,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelLandmarkRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.DelLandmarkResponse.SerializeToString,
            ),
            'ChangeLandmark': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeLandmark,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeLandmarkRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeLandmarkResponse.SerializeToString,
            ),
            'ListLandmark': grpc.unary_unary_rpc_method_handler(
                    servicer.ListLandmark,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListLandmarkRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListLandmarkResponse.SerializeToString,
            ),
            'ListDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevice,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListDeviceRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListDeviceResponse.SerializeToString,
            ),
            'ListUser': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUser,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListUserRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ListUserResponse.SerializeToString,
            ),
            'ChangeRole': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeRole,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeRoleRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeRoleResponse.SerializeToString,
            ),
            'Role': grpc.unary_unary_rpc_method_handler(
                    servicer.Role,
                    request_deserializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.RoleRequest.FromString,
                    response_serializer=vision__grpc_dot_vision__grpc_dot_manage__pb2.RoleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Manage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Manage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/AddDevice',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.AddDeviceRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.AddDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/DelDevice',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.DelDeviceRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.DelDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/ChangeDevice',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeDeviceRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddLandmark(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/AddLandmark',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.AddLandmarkRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.AddLandmarkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelLandmark(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/DelLandmark',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.DelLandmarkRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.DelLandmarkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeLandmark(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/ChangeLandmark',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeLandmarkRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeLandmarkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListLandmark(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/ListLandmark',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ListLandmarkRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ListLandmarkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/ListDevice',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ListDeviceRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ListDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/ListUser',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ListUserRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ListUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/ChangeRole',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeRoleRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.ChangeRoleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Role(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Manage/Role',
            vision__grpc_dot_vision__grpc_dot_manage__pb2.RoleRequest.SerializeToString,
            vision__grpc_dot_vision__grpc_dot_manage__pb2.RoleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)