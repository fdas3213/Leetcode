class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        
        self.dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        
        m, n = len(grid), len(grid[0])                
    
        def dfs(grid, i, j, m, n):
            count = 0
            grid[i][j] = -1
            
            for d in self.dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or grid[x][y]==0:
                    count += 1
                elif grid[x][y] == 1:
                    count += dfs(grid, x, y, m,n)
                
            return count
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(grid, i, j, m, n)
        
        return 0