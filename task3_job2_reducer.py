#!/usr/bin/env python3
import sys

#  company_totals to contain [total revenue, total trips, fleet size, total distance]
company_totals = [0.0, 0, 0, 0.0]
current_company = None

# use a set to keep track of unique taxi ids for a company
current_company_taxis = set()

#  input from job 1 taxi id, company, fare and distance
for line in sys.stdin:
    line = line.strip()  # remove leading/trailing whitespace
    if not line:
        continue

    fields = line.split('\t')  # split into the fields
    company = fields[0]
    taxi_id = fields[1]
    trips = int(fields[2])
    total_fare = float(fields[3])
    total_distance = float(fields[4])

    # capture the company_data for each new company read in.
    # shuffle and sort will be set up to sort records with same company to same reducer.
    if current_company is not None and current_company != company:
        total_rev, total_trips, fleet_size, total_dist = company_totals

        # calculate averages
        rev_per_taxi = total_rev / fleet_size
        avg_trip_dist = total_dist / total_trips

        print(f"{current_company}\t{total_rev}\t{total_trips}\t{fleet_size}\t{rev_per_taxi}\t{avg_trip_dist}")

        # reset the list to prepare for next company.
        company_totals = [0.0, 0, 0, 0.0]
        # reset the taxi set
        current_company_taxis = set()

    current_company = company

    # Aggregate company totals
    company_totals[0] += total_fare
    company_totals[1] += trips
    company_totals[3] += total_distance

    if taxi_id not in current_company_taxis:
        current_company_taxis.add(taxi_id)
        company_totals[2] += 1  # increase fleet count for each new taxi in company

if current_company:
    total_rev, total_trips, fleet_size, total_dist = company_totals
    rev_per_taxi = total_rev / fleet_size
    avg_trip_dist = total_dist / total_trips

    print(f"{current_company}\t{total_rev}\t{total_trips}\t{fleet_size}\t{rev_per_taxi}\t{avg_trip_dist}")