# This script generates the GTFS feed by running the gtfs_feed.py script with the appropriate command line arguments. Here is a sample code:

#!/bin/bash

python3 gtfs_feed.py \
    --mongo-uri mongodb://localhost:27017 \
    --mongo-database bus-tracking \
    --mongo-collection processed_locations \
    --output-file gtfs-feed.zip
