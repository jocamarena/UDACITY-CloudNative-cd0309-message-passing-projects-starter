import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload

location = location_pb2.LocationMessage(
    id = 1,
    person_id = 3,
    creation_time = "2020-07-07T10:37:06",
    longitude = "33.942791",
    latitude = "-118.410042",
)

response = stub.Create(location)