"""
Given an array with k elements(positive), ascend it (duplicate element is allowed)
"""
import logging
import math
logging.basicConfig(level=logging.INFO)

def counting_sort(arr):
    """
    k = max element of the arr 
    Time complexity: O(k) + O(n) + O( sum(1+counting_arr[i]) for i in range(k) == k + n )= O(n+k)
    
    basic counting sort: stability not guaranteed
    """
    if len(arr) <= 1:
        return arr
    max_element = arr[0]
    for x in arr[1:]:
        if x >= max_element:
            max_element = x
    logging.info(f"Max: {max_element}")
    counting_arr = [0 for _ in range(max_element)]
    for x in arr:
        counting_arr[x-1] += 1
    result = []
    for i,v in enumerate(counting_arr):
        if v != 0:
            result += [i] * v
    # TODO: trying to figure out a way to be more pythonic way
    # result = [ *([x[0]]*x[1]) for x in enumerate(counting_arr) if x[1] != 0]
    return result

class RadixSorter:
    """
    Radix sort: each integer is in base b eg. d = log(b)(k) where d is the maximum length will be assgined
    sort digit by digit from right to left aka less significant to more significant 


    O(n+k) per digit => TC is: O((n+b)*d) because in this case, the max value of each digit is b 
        => O((n+b)*log(b)(k))
        => the smaller the b is, the faster to sort per digit. Therefore minimize b to n 
        => O(2*n*log(n)(k)) where k could be some polynomial time of n eg. k = pow(n, const)?
        => O(const*n)
    """
    def __init__(self, arr, base=10):
        maximun = max(arr)
        self.cols = int(math.log(maximun, base))+1 
        self.base = base
        # initialize a matrix with n * k size
        self.radix_arr = [[0 for _ in range(self.cols)] for _ in range(len(arr))]
        # converting array of integer into matrix of size base * n 
        for row, x in enumerate(arr):
            temp = x
            start_index = self.cols-1
            while start_index>=0:
                self.radix_arr[row][start_index] = temp % base
                temp = temp // base
                start_index-=1
    
    def stable_counting_sort(self, arr):
        """
        arr: non-negative element
        stability guaranteed: keep the order as it is in the original array if they are equal
        return index mapping from origin to new
        """
        max_val = max(arr)
        result = dict.fromkeys(range(len(arr)))
        # initialize the pos list as the index of each first appear item
        how_many_element_smaller_then_k = [0 for _ in range(max_val+1)] # aka the new position of each first seen element
        counting = [0 for _ in range(max_val+1)]
        
        # O(n)
        for v in arr:
            counting[v] += 1

        num = len(arr)
        # O(n+k)
        for k in range(max_val, -1, -1):
            how_many_element_smaller_then_k[k] = num - counting[k]
            num = how_many_element_smaller_then_k[k]
        
        # O(n)
        for i,v in enumerate(arr):
            new_index = how_many_element_smaller_then_k[v]
            how_many_element_smaller_then_k[v]+=1    
            result[i] = new_index
        return result
    
    @staticmethod
    def remapping(arr, mapping):
        assert len(arr) == len(mapping)
        result = [[] for _ in range(len(arr))]
        for i in range(len(arr)):
            result[mapping[i]] = arr[i]
        return result
        
    def radix_sort(self):
        temp_radix = self.radix_arr
        col_ptr = len(self.radix_arr[0])-1
        while col_ptr >=0:
            arr = [x[col_ptr] for x in temp_radix]
            index_mapping = self.stable_counting_sort(arr)
            temp_radix = RadixSorter.remapping(temp_radix, index_mapping)
            col_ptr-=1
        return temp_radix
    def reverse_radix(self):
        """
        reverse radix to base 10 
        """

if __name__ == "__main__":
    # print(counting_sort([5,3,2,4,7,8,10,7,5,4,3,8,0,2,7,8,9,5,10,4,3,7,2]))
    radix = RadixSorter([5,3,2,4,7,8,10,15], base=2)
    # for x in radix.radix_arr:
    #     print(x)
    print(radix.radix_sort())