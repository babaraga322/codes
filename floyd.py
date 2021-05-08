# Python Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 9

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999


# Solves all pair shortest path
# via Floyd Warshall Algorithm

def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        if k in [0, 1, 3, 5]:
            print('K: ' + str(k))
            print(printSolution(dist))

        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=" ")
            if j == V - 1:
                print("")


graph = [[0, 5, 2, 4, 10, INF, INF, INF, INF],
         [5, 0, INF, 8, INF, INF, INF, INF, INF],
         [2, INF, 0, INF, 7, 5, INF, INF, INF],
         [4, 8, INF, 0, 6, INF, 2, INF, INF],
         [10, INF, 7, 6, 0, 3, 2, 3, INF],
         [INF, INF, 5, INF, 3, 0, INF, 2, 4],
         [INF, INF, INF, 2, 2, INF, 0, 3, INF],
         [INF, INF, INF, INF, 3, 2, 3, 0, 5],
         [INF, INF, INF, INF, INF, 4, INF, 5, 0]
         ]

floydWarshall(graph)
