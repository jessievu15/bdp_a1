#!/usr/bin/env python3
import sys

#  initialise empty dict
#  company_dict to contain
#  (company):[total revenue, total trips, fleet size, revenue per taxi, avg trip distance]
company_dict = {}
current_company = 0
current_taxi = 0
fleet = 0



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

    if company not in company_dict:
        # company_dict values = [total rev, total trips, fleet size, total dist, rev per taxi, avg trip dist]
        company_dict[company] = [0.0, 0, 0, 0.0, 0.0, 0.0]

    # work out totals for company
    if current_taxi != taxi_id:
        company_dict[company][0] += total_fare
        company_dict[company][1] += trips
        company_dict[company][2] += 1
        company_dict[company][3] += total_distance

    current_taxi = taxi_id

# work out the averages
for company in company_dict:
    company_dict[company][4] += (company_dict[company][0] / company_dict[company][2])
    company_dict[company][5] += (company_dict[company][3] / company_dict[company][1])
    print(f"{company}\t{company_dict[company][0]:.2f}\t{company_dict[company][1]}\t{company_dict[company][2]}\t{company_dict[company][3]:.2f}\t{company_dict[company][4]:.2f}\t{company_dict[company][5]:.2f}")
    current_company = company



