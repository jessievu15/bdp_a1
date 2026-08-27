import sys

max_rev = None
min_rev = None

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    revenue = float(fields[1])

    if max_rev is None or max_rev < revenue:
        max_rev = revenue

    if min_rev is None or min_rev > revenue:
        min_rev = revenue

band = (max_rev - min_rev)/3
cutoff_high = max_rev - band
cutoff_low = min_rev + band 

print(f'{cutoff_high}\t{cutoff_low}')