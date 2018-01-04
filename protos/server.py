import sys
import os
import sample_pb2
import sample_pb2_grpc
from concurrent import futures
from google.protobuf import empty_pb2
import time
import grpc


class SampleServer(sample_pb2_grpc.SampleServerServicer):
    def __init__(self):
        pass

    def Test(self, request, context):
        hage = 'me too'
        return sample_pb2.Pong(hage=hage)

    def Ding(self, request, context):
        return empty_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_SampleServerServicer_to_server(
        SampleServer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server is running")
    try:
        while True:
            time.sleep(100000)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
