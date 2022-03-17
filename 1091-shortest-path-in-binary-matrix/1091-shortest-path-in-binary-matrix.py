class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        #edge case
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
        
        #use a tuple of (x,y,dist) to not modify input
        queue = deque([(0,0,1)])
        visited = {(0,0)}
        
        while queue:
            x,y,dist = queue.popleft()
            if x==m-1 and y==n-1:
                return dist
            
            for d in dirs:
                new_x, new_y = x+d[0], y+d[1]
                if new_x<0 or new_y<0 or new_x>=m or new_y>=n or grid[new_x][new_y]!=0 or (new_x,new_y) in visited:
                    continue
                queue.append((new_x, new_y, dist+1))
                visited.add((new_x,new_y))
        
        return -1