# This script starts the data storage process by running the data_storage.py script with the appropriate command line arguments. Here is a sample code:
#!/bin/bash

python3 data_storage.py \
    --mongo-uri mongodb://localhost:27017 \
    --mongo-database bus-tracking \
    --mongo-collection processed_locations
