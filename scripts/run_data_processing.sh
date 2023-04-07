# This script runs the data processing pipeline by running the data_processing.py script with the appropriate command line arguments. Here is a sample code.

#!/bin/bash

python3 data_processing.py \
    --input-collection locations \
    --output-collection processed_locations \
    --time-window 5 \
    --distance-threshold 200
