import sys
from collections import defaultdict

total_trip = 0
max_fare = float('-inf')
min_fare = float('inf')
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
  