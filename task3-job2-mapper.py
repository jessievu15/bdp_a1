#!/usr/bin/env python3
import sys

#  initialise empty dict
#  taxi_dict to contain (taxi id, company):[trip count, total revenue, total distance for each taxi]
taxi_dict = {}

#  input from job 1 taxi id, company, fare and distance
for line in sys.stdin:
    line = line.strip()  # remove leading/trailing whitespace
    if not line:
        continue

    fields = line.split('\t')  # split into the fields
    taxi_id = fields[0]
    company = fields[1]
    fare = float(fields[2])
    distance = float(fields[3])

    # make (company, taxi_id) the key for taxi_dict
    key = (company, taxi_id)

    if key not in taxi_dict:
        taxi_dict[key] = [0, 0.0, 0.0]  # [trip count, total revenue, total distance]

    #  perform taxi level total calculations
    taxi_dict[key][0] += 1  # Trip count
    taxi_dict[key][1] += fare  # Total fare
    taxi_dict[key][2] += distance  # Total distance

# emit key value pairs
for (company, taxi_id), (trips, total_fare, total_distance) in taxi_dict.items():
    print(f"{company}\t{taxi_id}\t{trips}\t{total_fare}\t{total_distance}")

