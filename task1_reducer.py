#!/usr/bin/env python3
import sys

#  initialise empty dict
taxi_dict = {}
previous_taxi = None

# read input files line by line
for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    taxi_id = fields[0]
    trip_type = fields[1]
    trip_count = int(fields[2])
    max_fare = float(fields[3])
    min_fare = float(fields[4])
    total_fare = float(fields[5])

    # emit taxi_dict contents for previous taxi and reset taxi_dict when taxi_id changes
    if previous_taxi is not None and taxi_id != previous_taxi:
        for (t_id, t_type), (t_count, mx_fare, mn_fare, tot_fare) in taxi_dict.items():
            average_fare = tot_fare / t_count if t_count > 0 else 0.0
            print(f"{t_id}\t{t_type}\t{t_count}\t{mx_fare:.2f}\t{mn_fare:.2f}\t{average_fare:.2f}")
        taxi_dict = {}

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

    previous_taxi = taxi_id

# Emit last taxi results
if taxi_dict:
    for (t_id, t_type), (t_count, mx_fare, mn_fare, tot_fare) in taxi_dict.items():
        average_fare = tot_fare / t_count if t_count > 0 else 0.0
        print(f"{t_id}\t{t_type}\t{t_count}\t{mx_fare:.2f}\t{mn_fare:.2f}\t{average_fare:.2f}")
