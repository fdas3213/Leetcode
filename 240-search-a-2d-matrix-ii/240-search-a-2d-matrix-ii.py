class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def helper(up, down, left, right):
            if left>right or up>down:
                return False
            
            if matrix[up][left]>target or matrix[down][right]<target:
                return False
            
            mid = left+(right-left)//2
            
            row = up
            while row<=down and matrix[row][mid]<=target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return helper(row, down, left, mid-1) or helper(up, row-1, mid+1, right)
        
        m, n = len(matrix), len(matrix[0])

        return helper(0, m-1, 0, n-1)
            