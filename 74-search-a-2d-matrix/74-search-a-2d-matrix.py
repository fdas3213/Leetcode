class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        #O(log(M*N))
        start, end = 0, m*n-1
        while start <= end:
            mid = start + (end-start)//2
            row, col = mid//n, mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                start = mid+1
            else:
                end = mid-1
        return False