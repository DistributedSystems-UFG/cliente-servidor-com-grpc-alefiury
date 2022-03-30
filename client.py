import logging

import grpc
import strings_pb2
import strings_pb2_grpc
from constCS import *


def run():
    channel = grpc.insecure_channel(f"{HOST}:{PORT}")
    stub = strings_pb2_grpc.StringsOpsStub(channel)
    # Inputs
    first_string = input("Input your first string: ")
    second_string = input("Input your second string: ")
    operation = input("Choose one of the following operations -> Concat, Equal, Distance: ")

    # Operations
    if operation == 'Concat':
        response =  stub.ConcatStrings(strings_pb2.InString(str1=first_string, str2=second_string))
        print(f"Concatenated strings: {response.strout}")
    elif operation == 'Distance':
        response =  stub.LevenshteinDist(strings_pb2.InString(str1=first_string, str2=second_string))
        print(f"Levenshtein Distance: {response.message}")
    elif operation == 'Equal':
        response =  stub.Equal(strings_pb2.InString(str1=first_string, str2=second_string))
        print(response)
        if response:
            print("Strings are equal")
        else:
            print("Strings are not equal")

    else:
        response = "Operation does not exist"


if __name__ == '__main__':
    logging.basicConfig()
    run()
