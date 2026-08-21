import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def cal_avgdissimilarity(cluster_points, medoid):
    if not cluster_points:
        return 0.0
    total_distance = sum(euclidean_distance(point, medoid) for point in cluster_points)
    return total_distance / len(cluster_points)
