#
# This code is based off of the tutorial at https://grpc.io/docs/languages/python/quickstart/
#
from __future__ import print_function

import logging

import grpc
import helloworld_pb2 as messages
import helloworld_pb2_grpc as stubs


def run():
    print("Getting the weather ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = stubs.WeatherStub(channel)
        response = stub.GetWeather(messages.WeatherRequest(location="Galway"))
    print("The weather for " + response.location + " is: " + response.weather)


if __name__ == "__main__":
    logging.basicConfig()
    run()
