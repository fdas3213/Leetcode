class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[0,-1],[0,1],[1,0],[-1,0]]
        m, n = len(matrix), len(matrix[0])
        cache = [[0]*n for _ in range(m)]
        ans = 0
        
        def dfs(i:int, j:int):
            if cache[i][j]!=0:
                return cache[i][j]
            
            maxLen = 1
            
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or matrix[x][y]<=matrix[i][j]:
                    continue
                curMax = 1 + dfs(x,y)
                maxLen = max(maxLen, curMax)
            
            cache[i][j] = maxLen
                
            return maxLen
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
            
        return ans