#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split('\t')
    
    total_revenue, company_id, total_trips, fleet_size, revenue_per_taxi, avg_distance = fields
    print(f"{company_id}\t{total_revenue}\t{total_trips}\t{fleet_size}\t{revenue_per_taxi}\t{avg_distance}")