class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #edge case
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
        
        queue = deque()
        
        #use a tuple of (x,y) and update grid values on-the-fly
        queue.append((0,0))
        grid[0][0] = 1
        
        while queue:
            x,y = queue.popleft()
            if x==m-1 and y==n-1:
                return grid[x][y]
            
            for d in dirs:
                new_x, new_y = x+d[0], y+d[1]
                if new_x<0 or new_y<0 or new_x>=m or new_y>=n or grid[new_x][new_y]!=0:
                    continue
                grid[new_x][new_y] = grid[x][y] + 1
                queue.append((new_x, new_y))
        
        return -1