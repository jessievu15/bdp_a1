import sys

current_key = None # To track the current key being accumulated
current_count = 0
max_fare = float('-inf')
min_fare = float('inf')
sum_fare = 0.0

def cal_avg(key, total_trip, max_fare, min_fare, sum_fare):
    taxi_id, trip_type = key
    avg_fare = sum_fare / total_trip
    print(f"{taxi_id}\t{trip_type}\t{total_trip}\t{max_fare:.2f}\t{min_fare:.2f}\t{avg_fare:.2f}")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    taxi_id, trip_type, total, mx, mn, sm = line.split('\t')
    key = (taxi_id, trip_type)
    try:
        total, mx, mn, sm = int(total), float(mx), float(mn), float(sm)
    except ValueError:
        continue

    #for 340 medium 1 259.20 259.20 259.20, key = (340, "medium") 
    #for 354 long 1 15.00 15.00 15.00
    if key != current_key:
        if current_key is not None:
            cal_avg(current_key, current_count, max_fare, min_fare, sum_fare)
        current_key = key
        current_count, max_fare, min_fare, sum_fare = 0, float('-inf'), float('inf'), 0.0

    current_count += total
    max_fare = max(max_fare, mx)
    min_fare = min(min_fare, mn)
    sum_fare += sm

# to catch the last key after the loop ends
if current_key is not None:
    cal_avg(current_key, current_count, max_fare, min_fare, sum_fare)