#!/usr/bin/env python3
import sys
from collections import defaultdict

trip_type_dict = defaultdict(set)
#  empty list of total_trips, total_fare, fare_list, total_distance
taxi_dict = defaultdict(lambda: [0, 0.0, [], 0.0])
trip_type_list = ["short", "medium", "long"]

for line in sys.stdin:
    line = line.strip() # remove leading/trailing whitespace
    fields = line.split(',') # split into the fields

    # don't need pickup and dropoff information for now
    trip_id = fields[0]
    taxi_id = fields[1] 
    fare = float(fields[2])
    distance = float(fields[3])

    # check: all distance > 0
    if distance < 100:
        trip_type_dict[taxi_id].add(trip_type_list[0])
        taxi_dict[(taxi_id, trip_type_list[0])][0] += 1
        taxi_dict[(taxi_id, trip_type_list[0])][1] += fare
        taxi_dict[(taxi_id, trip_type_list[0])][2].append(fare)
        taxi_dict[(taxi_id, trip_type_list[0])][3] += distance
    elif distance >= 100 and distance < 200:
        trip_type_dict[taxi_id].add(trip_type_list[1])
        taxi_dict[(taxi_id, trip_type_list[1])][0] += 1
        taxi_dict[(taxi_id, trip_type_list[1])][1] += fare
        taxi_dict[(taxi_id, trip_type_list[1])][2].append(fare)
        taxi_dict[(taxi_id, trip_type_list[1])][3] += distance
    else:
        trip_type_dict[taxi_id].add(trip_type_list[2])
        taxi_dict[(taxi_id, trip_type_list[2])][0] += 1
        taxi_dict[(taxi_id, trip_type_list[2])][1] += fare
        taxi_dict[(taxi_id, trip_type_list[2])][2].append(fare)
        taxi_dict[(taxi_id, trip_type_list[2])][3] += distance

for (taxi_id, trip_type), (total_trip, total_fare, fare_list, total_distance) in taxi_dict.items():
    print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{max(fare_list)}\t{min(fare_list)}\t{total_fare}\t{total_distance}")


# taxiID that does not have all 3 trip types, the missing types presented as zero values for the categories
for taxi_id, trip_type in trip_type_dict.items():
    if len(trip_type) != 3:
        for type in trip_type_list:
            if type not in trip_type:
                print(f"{taxi_id}\t{type}\t0\t0.0\t0.0\t0.0\t0.0")

