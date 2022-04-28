class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        cnt = 0
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    #first row or first column
                    if i==0 or j==0:
                        cnt += 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
                        cnt += matrix[i][j]
        
        return cnt