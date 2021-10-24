# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from crawlab.grpc.entity import request_pb2 as entity_dot_request__pb2
from crawlab.grpc.entity import response_pb2 as entity_dot_response__pb2


class ModelBaseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetById = channel.unary_unary(
                '/grpc.ModelBaseService/GetById',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Get = channel.unary_unary(
                '/grpc.ModelBaseService/Get',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.GetList = channel.unary_unary(
                '/grpc.ModelBaseService/GetList',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.DeleteById = channel.unary_unary(
                '/grpc.ModelBaseService/DeleteById',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Delete = channel.unary_unary(
                '/grpc.ModelBaseService/Delete',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.DeleteList = channel.unary_unary(
                '/grpc.ModelBaseService/DeleteList',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.ForceDeleteList = channel.unary_unary(
                '/grpc.ModelBaseService/ForceDeleteList',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.UpdateById = channel.unary_unary(
                '/grpc.ModelBaseService/UpdateById',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Update = channel.unary_unary(
                '/grpc.ModelBaseService/Update',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.UpdateDoc = channel.unary_unary(
                '/grpc.ModelBaseService/UpdateDoc',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Insert = channel.unary_unary(
                '/grpc.ModelBaseService/Insert',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )
        self.Count = channel.unary_unary(
                '/grpc.ModelBaseService/Count',
                request_serializer=entity_dot_request__pb2.Request.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                )


class ModelBaseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForceDeleteList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDoc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelBaseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetById,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteById': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteById,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteList': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteList,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'ForceDeleteList': grpc.unary_unary_rpc_method_handler(
                    servicer.ForceDeleteList,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateById': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateById,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateDoc': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDoc,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=entity_dot_request__pb2.Request.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ModelBaseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelBaseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/GetById',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/Get',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/GetList',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/DeleteById',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/Delete',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/DeleteList',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ForceDeleteList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/ForceDeleteList',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/UpdateById',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/Update',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDoc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/UpdateDoc',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/Insert',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ModelBaseService/Count',
            entity_dot_request__pb2.Request.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
