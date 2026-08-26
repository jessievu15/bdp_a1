#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    
    company_id = fields[1]
    total_revenue = float(fields[2])
    total_trips = int(fields[3])
    fleet_size = int(fields[4])
    rev_per_taxi = float(fields[5])
    avg_trip_dist = float(fields[6])

    print(f"{fields[0]}\t{company_id}\t{total_revenue:.2f}\t{total_trips}\t{fleet_size}\t{rev_per_taxi:.2f}\t{avg_trip_dist:.2f}")