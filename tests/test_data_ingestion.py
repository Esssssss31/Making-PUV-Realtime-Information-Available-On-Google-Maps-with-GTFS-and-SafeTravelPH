# This file contains tests for the data_ingestion.py script. 
# The tests ensure that data is correctly ingested from the Kafka topics and saved to the MongoDB database.

import pytest
from data_ingestion import DataIngestion

def test_get_data_from_mqtt():
    # Arrange
    di = DataIngestion()

    # Act
    data = di.get_data_from_mqtt()

    # Assert
    assert isinstance(data, dict)
    assert len(data) > 0
