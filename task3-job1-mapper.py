#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()  # remove leading/trailing whitespace
    if not line:  # in case there are empty lines at start or end
        continue

    fields = line.split(',')  # split into fields

    # Check which input file the current line is from
    # data from Taxis.txt will have 4 fields when split
    # collect taxi id and company data
    if len(fields) == 4:
        taxi_id = fields[0]
        company = fields[1]

        # Tag data from Taxis.txt as A
        print(f"{taxi_id}\tA\t{company}")

    # data from Trips.txt will have 8 fields when split
    # collect taxi id, fare and distance
    else:
        taxi_id = fields[1]
        fare = fields[2]
        distance = fields[3]

        # Tag data from Trips.txt as B
        print(f"{taxi_id}\tB\t{fare}\t{distance}")