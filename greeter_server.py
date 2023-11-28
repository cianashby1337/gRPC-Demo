from concurrent import futures
import logging

import grpc
import helloworld_pb2 as messages
import helloworld_pb2_grpc as services


class Greeter(services.GreeterServicer):
    def SayHello(self, request, context):
        return messages.HelloReply(message="Hello, %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
