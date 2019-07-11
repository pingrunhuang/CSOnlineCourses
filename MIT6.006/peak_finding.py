"""
1d version:
given an array [1,2,3,4,5,2,7], find an element i such that a[i-1] <= a[i] and a[i+1]<=a[i]
Solution 1: brute forece O(n) 
Solution 2: divide and conquer strategy T(n) = T(n/2)+O(1) 
    T(1) = O(1), so T(n) = T(1) * (log(2)(n)) = log(2)(n)
    (this require the arrary to be ascending from left to n/2 and descending from n/2 to n)
    not guaranty to find one

2d version:
given a matrix [[1,2,3,4,5], [2,3,4,2,6], [3,1,3,5,6]] find an element (i,j) where (i,j)>=(i,j-1), (i,j)>=(i,j+1),
(i,j)>=(i-1,j), (i,j)>=(i+1,j)
solution 1: O(n*m) 
solution 2: T(n,m) = T(n,m/2) + O(n)=O(log(2)(m))*O(n) if you don't use divide and conquer strategy on each column, 
    O(log(m))*O(log(2)(n)) if use divide and conquer strategy on each col
"""


class PeakFinding:

    """
    why BST work: think about the case arr=[1,4,2,3,5,6,7,8,9,10], in the first iteration middle = 4,
    next arr[4-1]<arr[4] and arr[4]>arr[5] so we go to the righ part and search till the end. 10 is a valid peak
    """
    def devideConquer1d(self, arr):
        return self._devideConquer1d(arr, 0, len(arr)-1)
    
    def _devideConquer1d(self, arr, start_index, end_index):
        if start_index == end_index:
            return arr[start_index]
        if start_index < end_index:
            mid = start_index + (end_index-start_index)/2
            if arr[mid] < arr[mid+1]:
                return self._devideConquer1d(arr, mid, end_index)
            elif arr[mid] < arr[mid-1]:
                return self._devideConquer1d(arr, start_index, mid)
            else:
                return arr[mid]
        return -1

    def devideConquer2d(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        return self._devideConquer2d(mat, cols, 0, rows-1)

    def _is2DPeak(self, mat, i, j):
        # deal with corner case
        if i == 0 and mat[i][j] >= mat[i][j-1] and \
                mat[i][j] >= mat[i][j+1] and \
                mat[i][j] >= mat[i+1][j]:
                return True
        elif i == len(mat)-1 and mat[i][j] >= mat[i][j-1] and \
                mat[i][j] >= mat[i][j+1] and \
                mat[i][j] >= mat[i-1][j]:
                return True
        elif j == 0 and mat[i][j] >= mat[i+1][j] and \
                mat[i][j] >= mat[i-1][j] and \
                mat[i][j] >= mat[i][j+1]:
                return True
        elif j == len(mat[0])-1 and mat[i][j] >= mat[i+1][j] and \
                mat[i][j] >= mat[i-1][j] and \
                mat[i][j] >= mat[i][j-1]:
                return True
        elif mat[i][j] >= mat[i][j-1] and \
                mat[i][j] >= mat[i][j+1] and \
                mat[i][j] >= mat[i+1][j] and \
                mat[i][j] >= mat[i-1][j]:
                return True
        else:
            return False

    def _devideConquer2d(self, mat, cols, start_row, end_row):
        if start_row < end_row:
            mid_row = start_row + (end_row-start_row)/2
            for j in range(cols):
                if self._is2DPeak(mat, mid_row, j):
                    print(start_row, end_row)
                    return mat[mid_row][j]
                else:
                    # search the upper part
                    if mid_row>0 and mat[mid_row][j] < mat[mid_row-1][j]:
                        return self._devideConquer2d(mat, cols, start_row, mid_row)
                    # search the lower part
                    if mid_row<len(mat)-1 and mat[mid_row][j] < mat[mid_row+1][j]:
                        return self._devideConquer2d(mat, cols, mid_row+1, end_row)

        if start_row == end_row:
            # single row: find the global max
            for j in range(cols):
                if self._is2DPeak(mat, start_row, j):
                    return mat[start_row][j]
        return -1


        


if __name__ == "__main__":
    arr = [8,7,6,5,7,1]
    mat = [
        [0,1,2,3,4,5],
        [6,7,8,45,65,6],
        [10,12,13,14,15,14,3]
    ]
    finder = PeakFinding()
    print(finder.devideConquer2d(mat))