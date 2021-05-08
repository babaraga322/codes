import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist,src):
        mydict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G'}
        for i in range(len(dist)):
            print('From ' + mydict[src] + ' to ' + mydict[i] + ' = ' + str(dist[i]))

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist,src)


# Driver program
g = Graph(7)
g.graph = [[0, 1, 3, 0, 0, 10, 0],
           [1, 0, 1, 7, 5, 0, 2],
           [3, 1, 0, 9, 3, 0, 0],
           [0, 7, 9, 0, 2, 1, 12],
           [0, 5, 3, 2, 0, 2, 0],
           [10, 0, 0, 1, 2, 0, 0],
           [0, 2, 0, 12, 0, 0, 0],
           ]

g.dijkstra(0)
