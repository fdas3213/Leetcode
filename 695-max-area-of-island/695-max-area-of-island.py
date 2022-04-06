class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0,-1],[0,1],[1,0],[-1,0]]
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i, j):            
            # mask the island so that it's not counted again
            grid[i][j] = "*"
            visited.add((i,j))
            curSize = 1
            
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or grid[x][y]==0 or (x,y) in visited:
                    continue
                curSize += dfs(x, y)
            
            #visited[(i,j)] = curSize
            return curSize
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        
        return ans