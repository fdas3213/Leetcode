class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        #O(Mlog(N))
        for i in range(m):
            if target>matrix[i][n-1]:
                continue
            start, end = 0, n-1
            while start<=end:
                mid = start+(end-start)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    start = mid+1
                else:
                    end = mid-1
        
        return False