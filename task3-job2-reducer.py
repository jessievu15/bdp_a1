#!/usr/bin/env python3

import sys

company_dict={}
current_company = None
current_taxi = 0
fleet = set() # count of unique taxi ids

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split('\t')
    if len(fields) < 5:
        continue

    company = fields[0] 
    taxi_id = fields[1] 
    
    try:
        trips = int(fields[2])
        revenue = float(fields[3])
        distance = float(fields[4])
    except ValueError:
        continue  
 
    if company not in company_dict:
        company_dict[company] = [0.0, 0, set(), 0.0]
        
    if current_taxi != taxi_id:
        company_dict[company][0] += revenue
        company_dict[company][1] += trips
        company_dict[company][2].add(taxi_id)
        company_dict[company][3] +=distance
    
for company, (revenue, trips, taxis_set, distance) in company_dict.items():
    fleet = len(taxis_set)
    revenue_per_taxi = revenue/fleet
    avg_trip_distance = distance/trips 
    print(f"{company}\t{revenue:.2f}\t{trips}\t{fleet}\t{revenue_per_taxi:.2f}\t{avg_trip_distance:.2f}")

