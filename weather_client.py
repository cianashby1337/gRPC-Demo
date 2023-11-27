from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    print("Getting the weather ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.WeatherStub(channel)
        response = stub.GetWeather(helloworld_pb2.WeatherRequest(location="Galway"))
    print("The weather for " + response.location + " is: " + response.weather)


if __name__ == "__main__":
    logging.basicConfig()
    run()
