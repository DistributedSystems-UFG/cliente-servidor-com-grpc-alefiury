import logging
from concurrent import futures

import grpc
import strings_pb2
import strings_pb2_grpc
from utils import levenshtein

from constCS import *


class StringOps(strings_pb2_grpc.StringsOpsServicer):
    def ConcatStrings(self, request, context):
        """Concatenate two strings"""
        return strings_pb2.OutString(strout=request.str1+request.str2)

    def LevenshteinDist(self, request, context):
        """Calculates the levenshtein distance between two strings"""
        return strings_pb2.LevDist(message=levenshtein(request.str1, request.str2))

    def Equal(self, request, context):
        """Check if two strings are equal or not"""
        return strings_pb2.Comp(message=True if request.str1==request.str2 else False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    strings_pb2_grpc.add_StringsOpsServicer_to_server(StringOps(), server)
    server.add_insecure_port(PORT)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()