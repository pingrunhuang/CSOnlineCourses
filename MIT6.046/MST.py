"""
MST: minimum spanning tree 
The goal is to find the sub graph that has the path sum up to the lowest weight 
"""

class Vertex:
    def __init__(self, index, weight, next):
        self.index = index
        self.weight = weight
        self.next = next
    def hasNext(self):
        if self.next:
            return True
        return False
    def getNext(self):
        if self.hasNext():
            return self.next
        return None

import sys
class MST:
    def _prim(self, matrix, starting_v):
        visited_vertices = set([starting_v])
        all_vertices = set([i for i in range(len(matrix))])
        # init the distance_list
        distance_list = matrix[starting_v]

        while all_vertices != visited_vertices:
            # goal: update the distance list
            # first: find the vertex with the min distance and append
            min_index = all_vertices.difference(visited_vertices).pop()
            min_distance = distance_list[min_index]
            for i in all_vertices.difference(visited_vertices):
                if distance_list[i] < min_distance:
                    min_index = i
                    min_distance = distance_list[i]
            visited_vertices.add(min_index)
            # second: update distance list
            for v in all_vertices.difference(visited_vertices):
                distance_list[v] = min(matrix[min_index][v], distance_list[v])
        return distance_list
    
    def prim(self, matrix):
        result = sys.maxsize
        for vertex in range(len(matrix)):
            local_shortest_distance_list = self._prim(matrix, vertex)
            if sum(local_shortest_distance_list) < result:
                result = sum(local_shortest_distance_list)
                shortest_distance_list = local_shortest_distance_list
        print(shortest_distance_list)
        return result

if __name__ == "__main__":
    matrix = [
        [0, 1, 3, sys.maxsize, sys.maxsize, 3],
        [1, 0, 5, 1, sys.maxsize, sys.maxsize],
        [3,5,0,2,1, sys.maxsize],
        [sys.maxsize, 1,2,0,4,sys.maxsize],
        [sys.maxsize, sys.maxsize, 1,4,0,5,],
        [2,sys.maxsize, sys.maxsize, sys.maxsize, 5, 0]
    ]
    mst = MST()
    print(mst.prim(matrix))



        