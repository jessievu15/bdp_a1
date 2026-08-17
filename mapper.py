# Assumptions for Task 1
# - data is already clean
# - Taxi ID is always an integer
# - Input to mapper = Trips.txt file
# - Output from Reducer needs format Taxi ID, Trip Type, Total trips (per Trip Type), Max fare, Min fare, Avg fare
# Strategy
# Mapper to work out trip type based on distance conditions:
#   - Long = distance => 200
#   - Medium = 100 => distance < 200
#   - Short = distance < 100
# Mapper to work out Min, Max and total for each Trip Type per Taxi
# Reducer to work out the Average

import sys

# using a dictionary to map taxi id and trip type to count, max, min and sum.
current_taxi_id = None
current_trip_type = None
current_fare = 0.0

# for aggregation
trip_total = 0
total_fare = 0.0
max_fare = 0.0
min_fare = 0.0

for line in sys.stdin:
    #trip_type_dict = {} # Dictionary to collect Total trips, Sum, Max and Min for each Taxi ID and Trip type
    line = line.strip()
    fields = line.split(' ')
    trip_id, taxi_id, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = line.split("\t")

    # Mapping Trip Type
    if 200<=float(distance): trip_type = "Long"
    elif 100<=float(distance)<200: trip_type = "Medium"
    else: trip_type = "Short"

    # Work out Total trips, Sum, Max and Min for each Taxi ID and trip type.
    if current_taxi_id == taxi_id and current_trip_type == trip_type:
        if max_fare < float(fare):
            max_fare = float(fare)
        else:
            continue
        if min_fare > float(fare):
            min_fare = float(fare)
        else:
            continue
    else:
        max_fare = float(fare)
        min_fare = float(fare)
        current_taxi_id = taxi_id
        current_trip_type = trip_type

    total_fare += float(fare)
    trip_total += 1
    print('%s\t%s\t%s\t%s\t%s\t%s' % (current_taxi_id, current_trip_type, trip_total, max_fare, min_fare, total_fare))

# import sys
# from collections import defaultdict
#
# trip_type_dict = defaultdict(set)
# total_trip = 0
# total_fare = 0.0
# total_distance = 0.0
# taxi_dict = defaultdict(lambda: [total_trip, total_fare, total_distance])
# trip_type = ["short", "medium", "long"]
# for line in sys.stdin:
#     line = line.strip() # remove leading/trailing whitespace
#     fields = line.split(',') # split into the fields
#
#     # don't need pickup and dropoff information for now
#     trip_id = fields[0]
#     taxi_id = int(fields[1]) # consider coercing into integer so that we wont have issues later
#     fare = float(fields[2])
#     distance = float(fields[3])
#
#     # check: all distance > 0
#     if distance < 100:
#         trip_type_dict[taxi_id].add(trip_type[0])
#         taxi_dict[(taxi_id, trip_type[0])][0] += 1
#         taxi_dict[(taxi_id, trip_type[0])][1] += fare
#         taxi_dict[(taxi_id, trip_type[0])][2] += distance
#         print(f"{trip_id}\t{taxi_id}\t{fare}\t{distance}\t{trip_type[0]}")
#     elif distance >= 100 and distance < 200:
#         trip_type_dict[taxi_id].add(trip_type[1])
#         taxi_dict[(taxi_id, trip_type[1])][0] += 1
#         taxi_dict[(taxi_id, trip_type[1])][1] += fare
#         taxi_dict[(taxi_id, trip_type[1])][2] += distance
#         print(f"{trip_id}\t{taxi_id}\t{fare}\t{distance}\t{trip_type[1]}")
#     else:
#         trip_type_dict[taxi_id].add(trip_type[2])
#         taxi_dict[(taxi_id, trip_type[2])][0] += 1
#         taxi_dict[(taxi_id, trip_type[2])][1] += fare
#         taxi_dict[(taxi_id, trip_type[2])][2] += distance
#         print(f"{trip_id}\t{taxi_id}\t{fare}\t{distance}\t{trip_type[2]}")
#
# for (taxi_id, trip_type), (total_trip, total_fare, total_distance) in taxi_dict.items():
#     print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{total_fare}\t{total_distance}")
#
#
# '''# for combination of taxiID
# for taxi_id, trip_type in trip_type_dict.items():
#     if len(trip_type) != 3:
#         print(f"{taxi_id}\t{trip_type}\t0\t0.0\t0.0")'''

