"""
Priority queue is a set of elements 
    - insert(x)
    - max()
    - extract_max()
    - increase_key(x, k)

Heap is an array that implement the priority queue but satisfy the properties that binary tree has
One can imagine it as a tree 
"""

class MaxHeap:
    """
    same goes for MinHeap
    """
    def __init__(self, arr):
        """
        build max heap
        """
        self.heap = arr
        self.heap_size = len(arr)
        self.build_max_heap()
        self.is_max_heap = False

    def get_heap_size(self):
        return len(self.heap)

    def build_max_heap(self):
        """
        produce a max heap from an unordered array
        # start from n/2 to 0 for 2 reasons:
        # 1. the n/2 to n is already max heap (leaves)
        # 2. build from bottom up
        c is constant time of comparison
        level 1 has n/4 nodes (bottom up)
        level 2 has n/8 nodes 
        ...
        TC: O(n/4 (1 c)+n/8 (2 c)+n/16(3 c)+...+1 (lg n c)) 
            = O(n/4 (1/pow(2,0) + 2/pow(2,1) + ... + (k+1)/pow(2,k)))
            = O(n) 
            because (1/pow(2,0) + 2/pow(2,1) + ... + (k+1)/pow(2,k)) is convergent to a constant
        worst case of TC is O(nlgn)
        """
        for i in range(self.heap_size/2, -1, -1):
            self.max_heapify(i)
        self.is_max_heap = True

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def max_heapify(self, i):
        """
        correct the single violation of the heap property 
        TC is O(lg(n))
        """
        left_index = self.left_child(i)
        right_index = self.right_child(i)
         
        # find the largest element between parent, left and right
        largest = i
        if left_index < self.get_heap_size() and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        if right_index < self.get_heap_size() and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def parent(self, i):
        """
        get the parent's index of element i
        """
        return i/2
    
    def left_child(self, i):
        return 2*i
    
    def right_child(self, i):
        return 2*i+1
    
    def get_max(self):
        return self.heap[0]

    def extract_max(self):
        """
        pop the largest element from the heap and max heapify it again
        """
        result = self.heap[0]
        self.heap = self.heap[1:]
        self.build_max_heap()
        return result

    def insert(self, v):
        self.heap = [v] + self.heap
        self.build_max_heap()


    def heap_sort(self):
        """
        O(nlgn)
        """
        if not self.is_max_heap:
            self.build_max_heap()
        sorted_array = []
        while self.heap:
            sorted_array.append(self.get_max())
            self.swap(0, self.get_heap_size()-1)
            self.heap = self.heap[:self.heap_size-1]
            self.heap_size = self.heap_size-1
            self.build_max_heap()
        return sorted_array

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    arr = [4,1,3,2,16,9,10,14,8,7]
    heap = MaxHeap(arr)
    print(heap)
    print(heap.extract_max())
    print(heap)
    heap.insert(4)
    print(heap)
    print(heap.heap_sort())
