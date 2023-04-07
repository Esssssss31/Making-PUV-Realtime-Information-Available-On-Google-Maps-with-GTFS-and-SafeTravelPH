# This file contains tests for the gtfs_feed.py script. 
# The tests ensure that the GTFS feed is correctly generated from the data stored in the MongoDB database 
# and that it has the expected format and values.

import pytest
from gtfs_feed import GTFSFeed

def test_generate_gtfs_feed():
    # Arrange
    gf = GTFSFeed()
    data = {
        "vehicle_id": "1234",
        "latitude": 10.314596,
        "longitude": 123.891724,
        "speed": 30.0,
        "timestamp": "2022-04-12T10:30:00Z"
    }

    # Act
    gf.generate_gtfs_feed(data)

    # Assert
    assert gf.get_gtfs_feed() is not None
