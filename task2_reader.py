from task2_mapper import getCentroids


def checkCentroidsDistance(centroids, centroids1):

    if len(centroids) != len(centroids1): # mismatch number of centroids
        print(0)
        return

    for i in range(len(centroids)):
        if centroids[i][0] != centroids1[i][0] or centroids[i][1] != centroids1[i][1]:
            # if not exact match
            print(0)
            return

    print(1)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)
