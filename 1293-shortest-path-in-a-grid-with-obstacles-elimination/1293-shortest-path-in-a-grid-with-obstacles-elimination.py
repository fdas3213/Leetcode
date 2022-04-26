class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #bfs for shortest path
        queue = deque([(0,0,0,k)])
        #(x, y, n_steps, k_left)
        m, n = len(grid), len(grid[0])
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        visited.add((0, 0, k))
        while queue:
            x, y, n_steps, k_left = queue.popleft()
            if x==m-1 and y==n-1:
                return n_steps
            for d in dirs:
                new_x, new_y = x+d[0], y+d[1]
                #out of bound
                if new_x<0 or new_y<0 or new_x>=m or new_y>=n:
                    continue
                
                new_k = k_left-1 if grid[new_x][new_y]==1 else k_left
                #move on only if new_k>=0 and current (x,y,k) not visited 
                if new_k>=0 and (new_x,new_y,new_k) not in visited:
                    queue.append((new_x, new_y, n_steps+1, new_k))
                    visited.add((new_x, new_y, new_k))
        
        return -1