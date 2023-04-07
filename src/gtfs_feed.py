# here's a sample code for a gtfs_feed.py script that generates 
# a GTFS feed for a bus transit agency 
# using the gtfs-realtime-bindings and protobuf libraries

from gtfs_realtime_pb2 import FeedMessage
import protobuf_to_dict
import requests
import time

def generate_feed(bus_data):
    # Generate the GTFS feed message
    feed = FeedMessage()
    feed.header.gtfs_realtime_version = '2.0'
    feed.header.timestamp = int(time.time())
    for bus in bus_data:
        entity = feed.entity.add()
        entity.id = bus['id']
        entity.vehicle.trip.trip_id = bus['trip_id']
        entity.vehicle.position.latitude = bus['lat']
        entity.vehicle.position.longitude = bus['lon']
        entity.vehicle.position.bearing = bus['bearing']
        entity.vehicle.timestamp = int(bus['timestamp'])
    
    # Convert the feed message to a dictionary and serialize it as a protobuf message
    feed_dict = protobuf_to_dict.protobuf_to_dict(feed)
    serialized_feed = feed.SerializeToString()
    
    return serialized_feed

  # Note: This is just a basic example and it may need to be modified to fit the specific requirements of your project. 
  # Also, this example assumes that you already have the bus location data in a format that can be used to generate the GTFS feed.
  
