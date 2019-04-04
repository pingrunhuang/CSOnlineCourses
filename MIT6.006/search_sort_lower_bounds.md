# Goal of this course
- Find out an algo with linear time sorting
- have a sense of different sorting and searching lower bound time complexity

### Concepts
- root to leave: one time execution
- path length: the running time
- height of a tree: the worst case of execution
- decision tree is a form of binary search tree where n answers coorespond to n leaves.

### Searching lower bounds: O(lgN)
Intuition: searching is to find a target from root to leave in the worst case which is the height of the tree. Therefore it is O(lgN) complexity.


### Sorting lower bounds 
Reason: Essentailly, sorting will produce `n!` possibilities(permutation) where each possibilities will go to leave of a bst. Our mission is to find out the sorting order that we want.   
- prove 
since it is bst, the height is lg(leaves) which is also lg(n!) == lgn + lg(n-1) + ... + lg(2) + lg(1) >= sum(lgn) from n/2 to n >= sum(lg(n/2)) from n/2 to n == (n/2)*lg(n/2) + n/2 = O(nlgn)  
In fact, the lower bounds could be N*(lgN) - O(N) (sterling's formula: n! = sqrt(2*pi*N)*pow(N/e, N) => lg(n!) = lg(sqrt(2*pi*N)*pow(N/e, N))). Given this lower bound, we can have the following example of sorting algo which can achieve linear time sorting.
- radix sort: to understand radix sort, we need to first understand counting sort


