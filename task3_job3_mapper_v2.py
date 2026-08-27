#!/usr/bin/env python3
import sys

company_dict = {}
total_revenue_list = []
cutoff_high = None
cutoff_low = None

def revenue_level(total_revenue, cutoff_low, cutoff_high):
    # separate the each company total revenue by level: high (0), medium (1), low (2)
    if total_revenue > cutoff_high:
        return 0
    elif total_revenue > cutoff_low:
        return 1
    else:
        return 2

# read the boundaries from the txt file
with open("boundary.txt") as f:
    line = f.readline().strip()
    fields = line.split('\t')
    cutoff_high = float(fields[0])
    cutoff_low = float(fields[1])

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split('\t')

    company_id = fields[0]
    total_revenue = float(fields[1])
    total_trips = int(fields[2])
    fleet_size = int(fields[3])
    rev_per_taxi = float(fields[4])
    avg_trip_dist = float(fields[5])

    level = revenue_level(total_revenue, cutoff_low, cutoff_high)
    print(f"{level}\t{company_id}\t{total_revenue}\t{total_trips}\t{fleet_size}\t{rev_per_taxi}\t{avg_trip_dist}")


