# A script and used to publish to Google Transit

# This script reads data from processed_data.csv, generates trip_ids and stop_ids, sorts the data by stop_id and arrival_time, 
# and writes the GTFS data to CSV files in a gtfs directory. The resulting files are stops.txt, trips.txt, and stop_times.txt.

import csv
from datetime import datetime, timedelta
import os
import shutil

# Directory where the GTFS files will be stored
GTFS_DIRECTORY = 'gtfs'

# Load data from the processed data file
filename = 'data/processed_data.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]

# Create a dictionary to store stop_ids
stop_id_dict = {}

# Loop through the data and assign stop_ids
for row in data:
    stop_name = row[0]
    if stop_name not in stop_id_dict:
        stop_id_dict[stop_name] = len(stop_id_dict) + 1
    row.append(stop_id_dict[stop_name])

# Sort the data by stop_id, then by arrival time
data = sorted(data, key=lambda x: (x[-1], x[2]))

# Create a dictionary to store trip_ids
trip_id_dict = {}

# Generate GTFS trips and stop times
trips = []
stop_times = []
for row in data:
    stop_name = row[0]
    arrival_time = datetime.strptime(row[2], '%H:%M:%S')
    departure_time = datetime.strptime(row[3], '%H:%M:%S')
    stop_id = row[6]
    route_id = '1'
    
    # Generate trip_id
    if stop_id not in trip_id_dict:
        trip_id_dict[stop_id] = len(trip_id_dict) + 1
    trip_id = trip_id_dict[stop_id]
    
    # Add trip to trips list
    trips.append([trip_id, route_id])
    
    # Add stop time to stop_times list
    stop_time = [
        trip_id, 
        arrival_time.strftime('%H:%M:%S'), 
        departure_time.strftime('%H:%M:%S'), 
        stop_id, 
        len(stop_times) + 1
    ]
    stop_times.append(stop_time)

# Write GTFS data to CSV files
if os.path.exists(GTFS_DIRECTORY):
    shutil.rmtree(GTFS_DIRECTORY)
os.mkdir(GTFS_DIRECTORY)

# Write stops.txt file
with open(os.path.join(GTFS_DIRECTORY, 'stops.txt'), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
    for stop_name, stop_id in stop_id_dict.items():
        writer.writerow([stop_id, stop_name, '', ''])

# Write trips.txt file
with open(os.path.join(GTFS_DIRECTORY, 'trips.txt'), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['trip_id', 'route_id'])
    writer.writerows(trips)

# Write stop_times.txt file
with open(os.path.join(GTFS_DIRECTORY, 'stop_times.txt'), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['trip_id', 'arrival_time', 'departure_time', 'stop_id', 'stop_sequence'])
    writer.writerows(stop_times)

print('GTFS feed generated successfully!')
