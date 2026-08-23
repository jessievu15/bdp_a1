#!/usr/bin/env python3
import sys

current_taxi_id = None
company = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # split data into fields by tabs
    fields = line.split('\t')
    taxi_id = fields[0]
    tag = fields[1]
    data_fields = fields[2:]

    # Reset current taxi when reading new taxi id
    if taxi_id != current_taxi_id:
        current_taxi_id = taxi_id
        company = None

    # check if tag for the line is "A" - means its from Taxis.txt
    if tag == "A":
        company = data_fields[0]

    elif tag == "B":
        fare = float(data_fields[0])
        distance = float(data_fields[1])
        print(f"{taxi_id}\t{company}\t{fare}\t{distance}")



