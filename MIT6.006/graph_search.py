"""
Graph representation:

adjacency list: a linked list of all the adj of |V|
    for each vertex u, adj[u] stores all the neighbours of u

BFS:
bfs cares about the shortest path from a to b
    space complexity: O(|V| + |E|)
    Use case:
    1. cubes

DFS:
dfs cares about traversing all the possible vertices in graph
    Edge classification:
        1. tree edge: visit new vertex via edge (exists in both directed and undirected graph)
        2. forward edge: from node to descendant in tree (exists in directed graph)
        3. backward edge: from node to ancestor in tree (exists in both directed and undirected graph)
        4. cross edge: between 2 non-ancestor-related subtrees (exists in directed graph)

    time complexity: O(|V| + |E|)   
    use case:
    1. topological sort

"""
class BFSTemplate(object):
    def __init__(self, graph):
        self.graph = graph

    def solve(self, start):
        level = {start: 1}
        parent = {start: None}
        adj = self.graph[start]

        l = level[start]
        frontier_queue = [start]
        while frontier_queue:
            next_frontier_queue = []
            for v in frontier_queue:
                for adj in self.graph[v]:
                    if adj not in level:
                        level[adj] = l
                        parent[adj] = v
                        next_frontier_queue.append(adj)
            frontier_queue = next_frontier_queue
            l+=1
        return level, parent
    
    def hand_shake_lemma(self):
        """
        For directed graph: this will be |E|
        For un directed graph: this will be 2 * |E|
        """
        result = 0
        for v in self.graph:
            result += self.graph[v]
        return result

class DFSTemplate(object):
    """
    14
    """
    def __init__(self, graph):
        self.graph = graph
    
    def solve(self, start):
        parent = {} # to prevent not visit twice
        for adj in self.graph[start]:
            if adj not in parent:
                parent[adj] = None # init
                self._dfs(parent, adj) 
        return parent

    def _dfs(self, parent, v):
        for adj in self.graph[v]:
            if adj not in parent:
                parent[adj] = v
                self._dfs(parent, adj)
    
    def cycle_detection(self):
        """
        If backward edge exists, then cycle detected
        TODO: how to keep track of the backward edge????
        """
        pass

    def topological_sort(self):
        pass
    
    def job_schedule(self):
        pass

