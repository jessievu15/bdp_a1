import sys
from collections import defaultdict

total_trip = 0
max_fare = 0.0
min_fare = 0.0
sum_fare = 0.0
taxi_dict = defaultdict(lambda: [total_trip, max_fare, min_fare, sum_fare])

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = line.split(',')
    if len(fields) < 4:
        continue

    taxi_id = fields[1]
    fare = float(fields[2])
    distance = float(fields[3])

    if distance < 100:
        trip_type = "short"
    elif distance < 200:
        trip_type = "medium"
    else:
        trip_type = "long"

    t = taxi_dict[(taxi_id, trip_type)]
    t[0] += 1
    t[1] = max(t[1], fare)
    t[2] = min(t[2], fare)
    t[3] += fare
    
for (taxi_id, trip_type), (total_trip, max_fare, min_fare, sum_fare) in taxi_dict.items():
    print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{max_fare:.2f}\t{min_fare:.2f}\t{sum_fare:.2f}")
    
    
# import sys
# from collections import defaultdict

# trip_type_dict = defaultdict(set)
# total_trip = 0
# total_fare = 0.0
# total_distance = 0.0
# taxi_dict = defaultdict(lambda: [total_trip, total_fare, total_distance])
# trip_type = ["short", "medium", "long"]
# for line in sys.stdin:
#     line = line.strip() # remove leading/trailing whitespace
#     fields = line.split(',') # split into the fields

#     # don't need pickup and dropoff information for now
#     trip_id = fields[0]
#     taxi_id = fields[1] 
#     fare = float(fields[2]) 
#     distance = float(fields[3])

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

# for (taxi_id, trip_type), (total_trip, total_fare, total_distance) in taxi_dict.items():
#     print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{total_fare}\t{total_distance}")


# '''# for combination of taxiID
# for taxi_id, trip_type in trip_type_dict.items():
#     if len(trip_type) != 3:
#         print(f"{taxi_id}\t{trip_type}\t0\t0.0\t0.0")'''

