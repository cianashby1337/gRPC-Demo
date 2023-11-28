from concurrent import futures
import logging

import grpc
import helloworld_pb2 as messages
import helloworld_pb2_grpc as services

weather = [
    {"location":"Dublin", "weather":"rainy"},
    {"location":"Galway", "weather":"sunny"}
]

class Weather(services.WeatherServicer):
    def GetWeather(self, request, context):
        returnedWeather = "not listed"
        for location in weather:
            if(location["location"] == request.location): 
                returnedWeather = location["weather"]
                continue
            
        return messages.WeatherReply(location=request.location, weather=returnedWeather)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_WeatherServicer_to_server(Weather(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
