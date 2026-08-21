from task2_mapper import getCentroids

#check if distance of centroids and centroids1 is less than 1
def checkCentroidsDistance(centroids, centroids1):

    if len(centroids) != len(centroids1): # mismtach number of centroids
        print(0)
        return

    for i in range(len(centroids)):
        x_dist = abs(centroids[i][0] - centroids1[i][0])
        y_dist = abs(centroids[i][1] - centroids1[i][1])

        if x_dist >= 1 or y_dist >= 1:
            print(0)
            return

    print(1)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)
