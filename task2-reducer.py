#!/usr/bin/env python3
import sys
from pam import euclidean_distance, cal_avgdissimilarity


def process_cluster(points):
    if not points:
        return

    best_medoid = None
    min_cost = float('inf')

    for current_point in points:
        cost = cal_avgdissimilarity(points, current_point)
        if cost < min_cost:
            min_cost = cost
            best_medoid = current_point

    print(f"{best_medoid[0]}\t{best_medoid[1]}\t{len(points)}\t{min_cost:.2f}")


def calculate_new_medoids():
    current_index = None
    cluster_points = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        index, trip_id, distance, coords = line.split('\t')
        x, y = coords.split(',')
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            continue

        if index != current_index:
            if current_index is not None:
                process_cluster(cluster_points)
            current_index = index
            cluster_points = []

        cluster_points.append((x, y))

    if current_index is not None:
        process_cluster(cluster_points)


if __name__ == "__main__":
    calculate_new_medoids()