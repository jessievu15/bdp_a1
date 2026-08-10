#!/usr/bin/env python3
import sys

#  initialise empty dict
taxi_dict = {}

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    taxi_id = fields[0]
    trip_type = fields[1]
    trip_count = int(fields[2])
    max_fare = float(fields[3])
    min_fare = float(fields[4])
    total_fare = float(fields[5])

    if (taxi_id, trip_type) not in taxi_dict:
        taxi_dict[(taxi_id, trip_type)] = [0, None, None, 0.0]
    taxi_dict[(taxi_id, trip_type)][0] += trip_count

    if taxi_dict[(taxi_id, trip_type)][1] is None or max_fare > taxi_dict[(taxi_id, trip_type)][1]:
        # all trip max
        taxi_dict[(taxi_id, trip_type)][1] = max_fare

    if taxi_dict[(taxi_id, trip_type)][2] is None or min_fare < taxi_dict[(taxi_id, trip_type)][2]:
        # all trip min
        taxi_dict[(taxi_id, trip_type)][2] = min_fare
    
    taxi_dict[(taxi_id, trip_type)][3] += total_fare

for (taxi_id, trip_type), (trip_count, max_fare, min_fare, total_fare) in taxi_dict.items():
    average_fare = total_fare/trip_count if trip_count > 0 else 0.0
    print(f"{taxi_id}\t{trip_type}\t{trip_count}\t{max_fare:.2f}\t{min_fare:.2f}\t{average_fare:.2f}")

# python mapper_v2.py < Trips.txt | sort | python reducer_v2.py