"""
d[v] is the length of the current shortest path from starting vertex s.
delta[s,v] is the length of the shortest path from s to v
lemma: The relaxation operations maintains the invariant that d[v] >= delta[s,v]

proof:

Consider RELAX(u, v, w). By induction d[u] ≥ delta(s, u). By the triangle inequality, delta(s, v) ≤ delta(s, u) + delta(u, v). 
This means that delta(s, v) ≤ d[u] + w(u, v), since
d[u] ≥ delta(s, u) and w(u, v) ≥ delta(u, v). So setting d[v] = d[u] + w(u, v) is safe. 

one take away of dijkstra algorithm:
so called the invariant that d[v] >= delta[s,v]
"""
import sys
import heapq
import graphviz


class Cost(object):
    """
    The cost that should be spent from source vertex to target vertex
    """
    def __init__(self, weight, target):
        self.weight = weight
        self.target = target
    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight 

class DijkstraSPGraph(object):
    def __init__(self):
        self.vertices = {}
        self.min_cost_from_source_to = {} # shortest distance from start to target which is going to be updated
        self.predecessor_vertex = {}
        self.min_heap_cost_from_source_to = [] # priority queue: costs from source to target 
    
    def add_vertex(self, v_id, edges):
        self.vertices[v_id] = edges

    def relax(self, u, v):
        if self.min_cost_from_source_to[u] + self.vertices[u][v] < self.min_cost_from_source_to[v]:
            print("Start relax:", u, v)
            self.min_cost_from_source_to[v] = self.min_cost_from_source_to[u] + self.vertices[u][v]
            self.predecessor_vertex[v] = u
            for cost in self.min_heap_cost_from_source_to:
                if cost.target == v:
                    cost.weight = self.min_cost_from_source_to[v]
            heapq.heapify(self.min_heap_cost_from_source_to)
        else:
            print("No need to relax:", u, v)

    def initialize(self, source):
        self.min_cost_from_source_to.clear()
        self.predecessor_vertex.clear()
        self.min_heap_cost_from_source_to.clear()
        for vertex in self.vertices:
            if vertex == source:
                self.min_cost_from_source_to[vertex] = 0
                heapq.heappush(self.min_heap_cost_from_source_to, Cost(0, vertex))
            else:
                self.min_cost_from_source_to[vertex] = sys.maxsize
                heapq.heappush(self.min_heap_cost_from_source_to, Cost(sys.maxsize, vertex))
            self.predecessor_vertex[vertex] = None
        
    def dijkstra(self, start, target):
        self.initialize(source=start)

        while len(self.min_heap_cost_from_source_to)>0:
            # pop up the vertex with the least cost 
            cur_vertex = heapq.heappop(self.min_heap_cost_from_source_to).target

            # reached the target
            if target == cur_vertex:
                path = []
                ptr = target
                while self.predecessor_vertex[ptr]:
                    path.insert(0, ptr)
                    ptr = self.predecessor_vertex[ptr]
                path.insert(0, ptr)
                return path
            
            if self.min_cost_from_source_to[cur_vertex] == sys.maxsize: # All remaining vertices are inaccessible from source
                print('Path not found')
                continue
            
            for adjacent_vertex in self.vertices[cur_vertex]:
                self.relax(cur_vertex, adjacent_vertex)
        print('Path not found')
        return []
    def visualize(self, start, target):
        view = graphviz.Digraph("dijkstra",filename='process.gv', engine='sfdp')
        path = self.dijkstra(start, target)
        view.attr('node', shape='doublecircle')
        for vertex in path:
            view.node(vertex)
        view.attr('node', shape='circle')
        for vertex in self.vertices:
            if vertex not in path:
                view.node(vertex)
        for v in self.vertices:
            for adj in self.vertices[v]:
                view.edge(v, adj, label=str(self.vertices[v][adj]))
        view.view()


if __name__ == "__main__":
    # this is a directed graph, does it work with the undirected graph?
    g = DijkstraSPGraph()
    g.add_vertex('A', {'B': 7, 'C': 20})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    print(g.visualize('A', 'C'))
    print(g.min_cost_from_source_to)


    
