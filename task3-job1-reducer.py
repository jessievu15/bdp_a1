#!/usr/bin/env python3
import sys

current_taxi_id = None
company = None

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    taxi_id, tag, data = line.split('\t')

    # Reset current taxi when reading new taxi id
    if taxi_id != current_taxi_id:
        current_taxi_id = taxi_id
        company = None

    # check if tag for the line is "A" - means its from Taxis.txt
    if tag == "A":
        fields = data.split('\t')
        company = fields[0]

    elif tag == "B":
        fields = data.split('\t')
        fare = float(fields[0])
        distance = float(fields[1])

        if company is not None:
            print(f"{taxi_id}\t{company}\t{fare}\t{distance}")
