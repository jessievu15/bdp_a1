#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    taxi_id = fields[0]
    trip_type = fields[1]
    total_trip = int(fields[2])
    max_fare = float(fields[3])
    min_fare = float(fields[4])
    total_fare = float(fields[5])

    print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{max_fare:.2f}\t{min_fare:.2f}\t{total_fare/total_trip if total_trip > 0 else 0.00:.2f}")


# python mapper_v2.py < Trips.txt | sort | python reducer_v2.py