#!/usr/bin/env python3
import sys
from collections import defaultdict

trip_type_dict = defaultdict(set)
trip_type_list = ["short", "medium", "long"]

for line in sys.stdin:
    line = line.strip() # remove leading/trailing whitespace
    fields = line.split(',') # split into the fields

    # don't need pickup and dropoff information for now
    trip_id = fields[0]
    taxi_id = fields[1] 
    fare = float(fields[2])
    distance = float(fields[3])

    # already check: all distance > 0 and fare > 0
    if distance < 100:
        trip_type_dict[taxi_id].add(trip_type_list[0])
        # print out taxi ID, trip type, trip count, fare, distance
        print(f"{taxi_id}\t{trip_type_list[0]}\t1\t{fare}")
    elif distance >= 100 and distance < 200:
        trip_type_dict[taxi_id].add(trip_type_list[1])
        print(f"{taxi_id}\t{trip_type_list[1]}\t1\t{fare}")
    else:
        trip_type_dict[taxi_id].add(trip_type_list[2])
        print(f"{taxi_id}\t{trip_type_list[2]}\t1\t{fare}")

# taxiID that does not have all 3 trip types, the missing types presented as 0, 0.0 for the categories
for taxi_id, trip_type in trip_type_dict.items():
    if len(trip_type) != 3:
        for type in trip_type_list:
            if type not in trip_type:
                print(f"{taxi_id}\t{type}\t0\t0.0")

