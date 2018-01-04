import sys
import os
import sample_pb2
import sample_pb2_grpc
import grpc
from google.protobuf import empty_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = sample_pb2_grpc.SampleServerStub(channel)

    hoge = "i love you"
    fugas = [sample_pb2.Fuga(hago="hello"),
             sample_pb2.Fuga(hago="goodbye")]

    print("----- client is sending Ping to server -----")
    res = stub.Test(sample_pb2.Ping(hoge=hoge, fugas=fugas))
    print(res)
    print("------------- response returned ------------")
    print("----- client is sending Ding to server -----")
    res = stub.Ding(empty_pb2.Empty())
    print(res)
    print("------------- response returned ------------")


if __name__ == '__main__':
    run()
