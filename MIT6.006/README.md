# key points
[] hashing
    - chaining
    - table doubling 
    - open addressing
[] sorting with tree
    - bst sort
    - AVL tree sort
    - heap sort
    - counting sort
    - radix sort
[] graph
    - dijkstra
[]
[]

### graph notation
- G(V,E,W):
    E = O(V*V) at least one in and one out 
    d(v): current shortest path from source to v
    pi(v): predecessor of vertice v in the shortest path from source to v
    delta(u, v): length or total weight of a shortest path from u to v 
    
- relaxation 
suppose we have vertex u, v and weight between them called w(u,v).
if d[v] > d[u] + w(u,v):
    # update the value
    d[v] = d[u] + w(u,v)
    # update the predecessor 
    v.predecessor = u
- subpaths of a shortest path are shortest paths

Questions:
1. why the negative weight will cause issue?
In an undirected graph, a negative weight means both way is accessible from a to b, therefore it 
could possibly generate negative cycle(negative cycle is a directed cycle whose sum of edge weights is negative)

2. what is the problem of negative cycle?
essentially it is the negative cycle that will cause problems not the negative weight.
