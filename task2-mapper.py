#!/usr/bin/env python3
import sys
from pam import euclidean_distance


def get_medoid(file_path):
    medoids = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            medoid_id = int(parts[0])
            coords = [float(x) for x in parts[1].split(',')]
            medoids[medoid_id] = coords
    return medoids


def main():
    medoid_points = get_medoid('current_medoids.txt')

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        fields = line.split(',')
        if len(fields) < 8:
            continue

        trip_id = fields[0]
        dropoff_x = float(fields[6])
        dropoff_y = float(fields[7])
        point_coords = (dropoff_x, dropoff_y)

        best_medoid = None
        min_distance = float('inf')
        for m, coords in medoid_points.items():
            current_distance = euclidean_distance(point_coords, coords)
            if current_distance < min_distance:
                min_distance = current_distance
                best_medoid = m

        coords = ",".join(map(str, point_coords))
        print(f"{best_medoid}\t{trip_id}\t{min_distance:.2f}\t{coords}")


if __name__ == "__main__":
    main()