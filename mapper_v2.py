#!/usr/bin/env python3
import sys
from collections import defaultdict

#  initialise empty list of trip_count, max_fare, min_fare, total_fare
taxi_dict = defaultdict(lambda: [0, None, None, 0.0])

for line in sys.stdin:
    line = line.strip() # remove leading/trailing whitespace
    fields = line.split(',') # split into the fields

    # don't need pickup and dropoff information for now
    taxi_id = fields[1] 
    fare = float(fields[2])
    distance = float(fields[3])

    if distance < 100:
        trip_type = "short"
    elif distance >= 100 and distance < 200:
        trip_type = "medium"
    else:
        trip_type = "long"

    taxi_dict[(taxi_id, trip_type)][0] += 1 # update trip count

    if taxi_dict[(taxi_id, trip_type)][1] is None or fare > taxi_dict[(taxi_id, trip_type)][1]:
        # if max_fare is None or fare is greater than max_fare, update max_fare
        taxi_dict[(taxi_id, trip_type)][1] = fare
    if taxi_dict[(taxi_id, trip_type)][2] is None or fare < taxi_dict[(taxi_id, trip_type)][2]:
        # if min_fare is None or fare is less than min_fare, update min_fare
        taxi_dict[(taxi_id, trip_type)][2] = fare

    taxi_dict[(taxi_id, trip_type)][3] += fare # update total fare
    

for (taxi_id, trip_type), (trip_count, max_fare, min_fare, total_fare) in taxi_dict.items():
    print(f"{taxi_id}\t{trip_type}\t{trip_count}\t{max_fare}\t{min_fare}\t{total_fare}")


