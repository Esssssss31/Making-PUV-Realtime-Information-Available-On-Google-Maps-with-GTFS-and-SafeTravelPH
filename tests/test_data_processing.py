# This file contains tests for the data_processing.py script. 
# The tests ensure that the data processing functions are correctly implemented and that the output data has the expected format and values.

import pytest
from data_processing import DataProcessing

def test_process_data():
    # Arrange
    dp = DataProcessing()
    raw_data = {
        "vehicle_id": "1234",
        "latitude": 10.314596,
        "longitude": 123.891724,
        "speed": 30.0,
        "timestamp": "2022-04-12T10:30:00Z"
    }

    # Act
    processed_data = dp.process_data(raw_data)

    # Assert
    assert isinstance(processed_data, dict)
    assert len(processed_data) == 5
    assert processed_data['vehicle_id'] == '1234'
    assert processed_data['latitude'] == 10.3146
    assert processed_data['longitude'] == 123.8917
    assert processed_data['speed'] == 30.0
    assert processed_data['timestamp'] == '2022-04-12T10:30:00Z'
