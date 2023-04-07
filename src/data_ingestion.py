# A Python script that receives real-time data from the mobile app via MQTT 
# and stores it in Apache Kafka.
# here's a sample code for a data_ingestion.py script that reads real-time location 
# data from a Kafka topic and saves it to a MongoDB database
# This script uses the kafka-python library to create a Kafka consumer that reads messages 
# from a bus-location topic and deserializes the JSON data. 
# It then uses the pymongo library to create a connection to a local MongoDB database and collection, 
# and saves each message as a document in the bus_location collection.
# Note that this is just a basic example and you may need to modify it 
# to fit your specific requirements and data schema. 
# You will also need to install the necessary libraries and configure your Kafka and MongoDB instances accordingly.

import json
from kafka import KafkaConsumer
from pymongo import MongoClient

# Kafka consumer configuration
consumer = KafkaConsumer(
    'bus-location',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# MongoDB client configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['transit']
collection = db['bus_location']

# Main ingestion loop
for message in consumer:
    data = message.value
    collection.insert_one(data)
    print(f"Saved data to MongoDB: {data}")
