#!/usr/bin/env python3
import sys
from math import sqrt

# get initial centroids from a txt file and add them to a list
def getCentroids(filename):
    centroids = []

    with open(filename) as f:
        line = f.readline()
        while line:
            if line:
                try:
                    line = line.strip()
                    cord = line.split('\t')
                    if len(cord) == 2: # skip line 1 of initialization.txt file
                        centroids.append([float(cord[0]), float(cord[1])])
                except:
                    break
            else:
                break
            line = f.readline()
    f.close()
    return centroids

# create clusters based on initial centroids
def createClusters(centroids):
    for line in sys.stdin:
        line = line.strip()
        fields = line.split(',')
        min_dist = 100000000000000
        index = -1
        closest_centroid = None

        for i, centroid in enumerate(centroids):
            try:
                # get dropoff cordinates
                x_cord = float(fields[6])
                y_cord = float(fields[7])
            except ValueError:
                continue

            cur_dist = sqrt(pow(x_cord - centroid[0], 2) + pow(y_cord - centroid[1], 2))

            if cur_dist <= min_dist:
                min_dist = cur_dist
                # closest_centroid = centroid
                index = i

        # print("%s\t%s\t%s\t%s\t%s" % (closest_centroid[0], closest_centroid[1], x_cord, y_cord))
        print("%s\t%s\t%s" % (index, x_cord, y_cord))     
if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    createClusters(centroids)