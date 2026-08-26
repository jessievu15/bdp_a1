#!/usr/bin/env python3
import sys
from math import sqrt

def processCluster(current_cluster, points):

    min_cost = 100000000000000
    
    for i, current_point in enumerate(points):
        total = 0.0

        for j, next_point in enumerate(points):
            if i == j: # same index then skip
                continue
            total += sqrt(pow(current_point[0] - next_point[0], 2) + pow(current_point[1] - next_point[1], 2))

        if len(points) == 1: # if cluster only has 1 point
            mediod = points[0]
            avg_dissimilarity = 0.0
        else:
            avg_dissimilarity = total/(len(points)-1)

        if avg_dissimilarity < min_cost:
            # record points with the lowest average dismmilarity
            min_cost = avg_dissimilarity
            mediod = current_point

    print("%s\t%s\t%s\t%.2f" % (mediod[0], mediod[1], len(points), min_cost))     

def calculateNewCentroids():
    current_cluster = None
    points = []

    for line in sys.stdin:
        line = line.strip()

        index, x, y = line.split('\t')

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            continue

        if current_cluster == index:
            points.append((x, y))
        else:
            if current_cluster is not None:
                processCluster(current_cluster, points)
            current_cluster = index
            points = [(x, y)]

    if current_cluster is not None:
        processCluster(current_cluster, points)

if __name__ == "__main__":
    calculateNewCentroids()