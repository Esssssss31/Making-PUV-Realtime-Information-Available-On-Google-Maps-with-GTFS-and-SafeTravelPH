# This script starts the data ingestion process by running the data_ingestion.py script with the appropriate command line arguments. Here is a sample code.

#!/bin/bash

python3 data_ingestion.py \
    --kafka-server localhost:9092 \
    --kafka-topic bus-locations \
    --mongo-uri mongodb://localhost:27017 \
    --mongo-database bus-tracking \
    --mongo-collection locations
