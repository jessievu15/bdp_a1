#!/usr/bin/env python3
import sys
from collections import defaultdict

#  empty list of total_trips, total_fare, fare_list, total_distance
taxi_dict = defaultdict(lambda: [0, [], 0.0])
trip_type_list = ["short", "medium", "long"]

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    taxi_id = fields[0]
    trip_type = fields[1]
    trip_count = int(fields[2])
    fare = float(fields[3])

    taxi_dict[(taxi_id, trip_type)][0] += trip_count
    taxi_dict[(taxi_id, trip_type)][1].append(fare)
    taxi_dict[(taxi_id, trip_type)][2] += fare

for (taxi_id, trip_type), (total_trip, fare_list, total_fare) in taxi_dict.items():
    max_fare = max(fare_list) if fare_list else 0.0
    min_fare = min(fare_list) if fare_list else 0.0
    average_fare = total_fare/total_trip if total_trip > 0 else 0.0
    print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{max_fare:.2f}\t{min_fare:.2f}\t{average_fare:.2f}")
    

