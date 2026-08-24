#!/usr/bin/env python3

import sys
from collections import defaultdict

total_trips = 0
total_revenue = 0.0
total_trip_distance = 0.0 #sum of trip distance / total trips

taxi_dict = defaultdict(lambda:[total_revenue, total_trips, total_trip_distance])

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split(',')
    if len(fields) < 4:
        continue

    taxi_id = fields[0]
    company = fields[1]
    try:
        fare = float(fields[2])
        distance = float(fields[3])
    except ValueError:
        continue  # Skip lines with invalid fare or distance values
    
    # Update the taxi information
    t = taxi_dict[(taxi_id, company)]
    t[0] += 1           #sum trips for each taxi
    t[1] += fare        #sum revenue for each taxi
    t[2] += distance    #sum distance for each taxi

for (taxi_id, company), (total_trips, total_revenue, total_trip_distance) in taxi_dict.items():
    print(f"{company}\t{taxi_id}\t{total_trips}\t{total_revenue:.2f}\t{total_trip_distance:.2f}")