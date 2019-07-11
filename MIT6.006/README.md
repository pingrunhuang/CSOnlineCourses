# Unit 1: Introduction
- Lecture 1 – Algorithmic Thinking, Peak Finding (8 Sep 2011) | readings: 1, 3, D.1

- Lecture 2 – Models of Computation, Python Cost Model, Document Distance (13 Sep 2011) | readings: 1, 3, Python Cost Model
# Unit 2: Sorting and Trees
- Lecture 3 – Insertion Sort, Merge Sort (15 Sep 2011) | readings: 1.2, 2.1-2.3, 4.3-4.6

- Lecture 4 – Heaps and Heap Sort (20 Sep 2011) | readings: 6.1-6.4

- Lecture 5 – Binary Search Trees, BST Sort (22 Sep 2011) | readings: 10.4, 12.1, 12.2, 12.3

- Lecture 6 – AVL Trees, AVL Sort (27 Sep 2011) | readings: 13.2, 14

- Lecture 7 – Counting Sort, Radix Sort, Lower Bounds for Sorting and Searching (29 Sep 2011) | readings 8.1-8.3

# Unit 3: Hashing
- Lecture 8 – Hashing with Chaining (4 Oct 2011) | readings: 11.1-11.3
- Recitation 8 – Simulation Algorithms (5 Oct 2011)

- Lecture 9 – Table Doubling, Karp-Rabin (6 Oct 2011) | readings: 17
- Recitation 9b – DNA Sequence Matching (12 Oct 2011) 

- Lecture 10 – Open Addressing, Cryptographic Hashing (13 Oct 2011) | readings: 11.4
- Recitation 10b – Quiz 1 Review (14 Oct 2011)


# Unit 4: Numerics
- Lecture 11 – Integer Arithmetic, Karatsuba Multiplication (20 Oct 2011) | recitation notes on algorithm design
- Lecture 12 – Square Roots, Newton's Method (25 Oct 2011)

# Unit 5: Graphs
- Lecture 13 – Breadth-First Search (BFS) (27 Oct 2011) | readings: 22.1-22.2, B.4
- Lecture 14 – Depth-First Search (DFS), Topological Sorting (1 Nov 2011) | readings: 22.3-22.4

# Unit 6: Shortest Paths
- Lecture 15 – Single-Source Shortest Paths Problem (3 Nov 2011) | readings: 24.0, 24.5
- Lecture 16 – Dijkstra (8 Nov 2011) | readings: 24.3
- Lecture 17 – Bellman-Ford (10 Nov 2011) | readings: 24.1-24.2
- Lecture 18 – Speeding up Dijkstra (15 Nov 2011)
- Recitation 18b – Quiz 2 Review (16 Oct 2011)


# Unit 7: Dynamic Programming
- Lecture 19 – Memoization, Subproblems, Guessing, Bottom-up; Fibonacci, Shortest Paths (22 Nov 2011) | readings: 15.1, 15.3
- Lecture 20 – Parent Pointers; Text Justification, Perfect-Information Blackjack (29 Nov 2011) | readings: 15.3, Problem 15-4, Blackjack rules
- Lecture 21 – String Subproblems, Pseudopolynomial Time; Parenthesization, Edit Distance, Knapsack (1 Dec 2011) | readings: 15.1, 15.2, 15.4
- Lecture 22 – Two Kinds of Guessing; Piano/Guitar Fingering, Tetris Training, Super Mario Bros. (6 Dec 2011)

# Unit 8: Advanced Topics
- Lecture 23 – Computational Complexity (8 Dec 2011) | readings: 34.1-34.3
- Lecture 24 – Algorithms Research Topics (13 Dec 2011)

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
