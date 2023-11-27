from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

weather = [
    {"location":"Dublin", "weather":"rainy"},
    {"location":"Galway", "weather":"sunny"}
]

class Weather(helloworld_pb2_grpc.WeatherServicer):
    def GetWeather(self, request, context):
        returnedWeather = "not listed"
        for location in weather:
            if(location["location"] == request.location): 
                returnedWeather = location["weather"]
                continue
            
        return helloworld_pb2.WeatherReply(location=request.location, weather=returnedWeather)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_WeatherServicer_to_server(Weather(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
