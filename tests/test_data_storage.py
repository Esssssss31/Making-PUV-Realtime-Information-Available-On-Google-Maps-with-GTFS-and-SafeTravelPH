# This file contains tests for the data_storage.py script. 
# The tests ensure that data is correctly saved and retrieved from the MongoDB database.

import pytest
from data_storage import DataStorage
from pymongo import MongoClient

@pytest.fixture(scope='module')
def mongo_client():
    client = MongoClient('mongodb://localhost:27017/')
    yield client
    client.drop_database('test_db')

def test_save_data_to_mongodb(mongo_client):
    # Arrange
    ds = DataStorage(mongo_client, 'test_db')
    data = {
        "vehicle_id": "1234",
        "latitude": 10.314596,
        "longitude": 123.891724,
        "speed": 30.0,
        "timestamp": "2022-04-12T10:30:00Z"
    }

    # Act
    ds.save_data_to_mongodb(data)

    # Assert
    assert mongo_client.test_db.raw_data.find_one({'vehicle_id': '1234'})
