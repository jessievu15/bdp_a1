#!/usr/bin/env python3
import sys
import os

# Get the name of the file currently being processed by Hadoop.
filepath = os.environ.get('mapreduce_map_input_file', '').lower()

for line in sys.stdin:
    line = line.strip()  # remove leading/trailing whitespace
    if not line:  # in case there are empty lines at start or end
        continue

    fields = line.split(',')  # split into the fields

    # Check which input dataset current line is from
    if "taxis" in filepath:
        # Input 1: Taxis.txt (only need taxi id and company)
        taxi_id = fields[0]
        company = fields[1]
        # Tag data from Taxis.txt as A
        print(f"{taxi_id}\tA\t{company}")

    else:
        # Input 2: Trips.txt (only need taxi id, fare and distance)
        taxi_id = fields[1]
        fare = float(fields[2])
        distance = float(fields[3])
        # Tag data from Trips.txt as B
        print(f"{taxi_id}\tB\t{fare}\t{distance}")

