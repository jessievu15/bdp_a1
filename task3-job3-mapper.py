#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split('\t')
    if len(fields) < 6:
        continue
    
    company_id,total_revenue, total_trips, fleet_size, revenue_per_taxi, avg_distance = fields
    try:  
        total_revenue = float(total_revenue)
    except ValueError:
        continue  
    
    print(f"\t{float(total_revenue):.2f}\t{company_id}\t{total_trips}\t{fleet_size}\t{revenue_per_taxi}\t{avg_distance}")