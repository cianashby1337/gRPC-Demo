from __future__ import print_function

import logging

import grpc
import helloworld_pb2 as message
import helloworld_pb2_grpc as stubs


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = stubs.GreeterStub(channel)
        response = stub.SayHello(message.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
