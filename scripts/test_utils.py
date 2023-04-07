# In this example, we're testing two functions from utils.py: clean_bus_id and format_time.

# In the test_clean_bus_id method, we're passing in a couple of bus IDs with different formats, 
# and checking that the clean_bus_id function is returning the expected result (i.e. just the numeric portion of the ID).

# In the test_format_time method, we're passing in a couple of timestamps and checking that the format_time function 
# is correctly converting them to the desired time format.

# Note that these are just example tests, and you would likely want to add more tests for all of the utility functions
# used in your project to ensure that they are working correctly.

import unittest
from api.utils import clean_bus_id, format_time

class TestUtils(unittest.TestCase):
    def test_clean_bus_id(self):
        bus_id = 'bus-123'
        expected_result = '123'
        self.assertEqual(clean_bus_id(bus_id), expected_result)

        bus_id = 'shuttle_456'
        expected_result = '456'
        self.assertEqual(clean_bus_id(bus_id), expected_result)

    def test_format_time(self):
        timestamp = 1618763800  # April 18, 2021 10:50:00 AM UTC
        expected_result = '10:50:00'
        self.assertEqual(format_time(timestamp), expected_result)

        timestamp = 1618782000  # April 18, 2021 3:00:00 PM UTC
        expected_result = '15:00:00'
        self.assertEqual(format_time(timestamp), expected_result)
