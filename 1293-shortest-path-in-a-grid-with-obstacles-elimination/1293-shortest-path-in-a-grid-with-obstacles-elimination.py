class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #shortest path bfs.
        
        m, n =len(grid), len(grid[0])
        # (x, y, step, number of available eliminations)
        queue = deque([(0, 0, 0, k)])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        # use visited
        visited = set()
        #need to add k together with coordinate to the visited set because there might exist multiple path from (0,0) to p, and the number of obstacles on the path is different, so we need to add k as well
        visited.add((0,0,k))
        ans = m*n
        while queue:
            x, y, step, cnt = queue.popleft()
            if x==m-1 and y==n-1:
                return step
            
            for d in dirs:
                new_x, new_y = x+d[0],y+d[1]
                if new_x<0 or new_y<0 or new_x>=m or new_y>=n:
                    continue
                
                new_cnt = cnt-grid[new_x][new_y]
                if new_cnt>=0 and (new_x, new_y, new_cnt) not in visited:
                    queue.append((new_x,new_y,step+1,new_cnt))
                    visited.add((new_x,new_y, new_cnt))
        
        return -1
            