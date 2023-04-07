# Here's a sample code for a data_processing.py script that reads data from a MongoDB collection, transforms it into GTFS format, and saves it to a file.
# This code reads data from a MongoDB collection, transforms it into GTFS format, and saves it to a CSV file. 
# It first sets up the MongoDB client and GTFS output file configuration. 
#It defines a function to format time strings as HH:MM:SS. Then, it loops through the MongoDB collection and processes each document. 
# It calculates the elapsed time between the start time and the timestamp of each document, and uses this to generate the stop ID and stop sequence. 
# Finally, it writes each row to the CSV file. T
# The output file contains data in the format required by the Google Transit Feed Specification, which can be used to publish transit data to Google Transit.

import csv
from pymongo import MongoClient
from datetime import datetime, timedelta

# MongoDB client configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['transit']
collection = db['bus_location']

# GTFS output file configuration
filename = 'gtfs_data.csv'
header = ['trip_id', 'arrival_time', 'departure_time', 'stop_id', 'stop_sequence', 'route_id']
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# Define a function to format time strings as HH:MM:SS
def format_time(t):
    dt = datetime.fromtimestamp(t)
    return dt.strftime('%H:%M:%S')

# Main data processing loop
start_time = None
for doc in collection.find().sort('timestamp'):
    bus_id = doc['bus_id']
    lat = doc['lat']
    lon = doc['lon']
    timestamp = doc['timestamp']
    
    if start_time is None:
        start_time = timestamp
    
    elapsed_time = (timestamp - start_time) // 60
    arrival_time = format_time(timestamp)
    departure_time = format_time(timestamp)
    stop_id = f"{bus_id}_{elapsed_time}"
    stop_sequence = elapsed_time + 1
    route_id = bus_id
    
    row = [bus_id, arrival_time, departure_time, stop_id, stop_sequence, route_id]
    
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

print(f"GTFS data saved to {filename}")

