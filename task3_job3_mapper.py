#!/usr/bin/env python3
import sys

company_dict = {}
total_revenue_list = []


with open("job2_output.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        fields = line.split('\t')
        total_revenue_list.append(float(fields[1]))

# calculate the cutoff benchmark to separate the record into 3 revenue level: high (0), medium (1), low (2)
min_rev = min(total_revenue_list)
max_rev = max(total_revenue_list)
band = (max_rev - min_rev)/3
cutoff_high = max_rev - band
cutoff_low = min_rev + band

def revenue_level(total_revenue):
    
    if total_revenue >= cutoff_high:
        return 0
    elif total_revenue >= cutoff_low:
        return 1
    else:
        return 2

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    company_id = fields[0]
    total_revenue = float(fields[1])
    total_trips = int(fields[2])
    fleet_size = int(fields[3])
    rev_per_taxi = float(fields[4])
    avg_trip_dist = float(fields[5])

    level = revenue_level(total_revenue)
    print(f"{level}\t{company_id}\t{total_revenue}\t{total_trips}\t{fleet_size}\t{rev_per_taxi}\t{avg_trip_dist}")


