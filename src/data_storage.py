# Here's a sample code for a data_storage.py script that receives real-time bus location data via MQTT and saves it to a MongoDB database.
# This is just a basic example and it may need to be modified to fit the specific requirements of your project.

import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import time

# MQTT client configuration
broker_address = "localhost"
topic = "bus_location"
client = mqtt.Client()
client.connect(broker_address)

# MongoDB client configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['transit']
collection = db['bus_location']

# Define a callback function to handle incoming MQTT messages
def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode('utf-8'))
    bus_id = payload['bus_id']
    lat = payload['lat']
    lon = payload['lon']
    timestamp = time.time()
    doc = {'bus_id': bus_id, 'lat': lat, 'lon': lon, 'timestamp': timestamp}
    collection.insert_one(doc)

# Subscribe to the MQTT topic and start listening for messages
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
