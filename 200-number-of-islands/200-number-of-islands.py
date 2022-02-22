class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        count = 0
        
        def dfs(i:int, j:int):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!='1':
                return
            
            grid[i][j] = "*"
            for d in dirs:
                x = i+d[0]
                y = j+d[1]
                dfs(x,y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count += 1
                    dfs(i,j)
        
        return count