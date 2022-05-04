class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        2-step approach:
        1. find two islands, and mark 1st island with a 'X' (dfs)
        2. for each X, find a Y with shortest path (bfs)
        """
        
        #step 1.
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        m, n = len(grid), len(grid[0])
        queue = deque([])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(i, j, mark):
            #denote the current grid with a mark
            grid[i][j] = mark
            queue.append((i,j))
            visited[i][j] = True
            
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or grid[x][y]!=1:
                    continue
                dfs(x, y, mark)
        
        #we only need to mark the first island to separate it from the second one
        marked = False
        for i in range(m):
            for j in range(n):
                if marked:
                    #stop the loop after marking the first island
                    break
                if grid[i][j] == 1:
                    marked = True
                    dfs(i, j, 'X')
                        
        #step 2: bfs
        #keep expanding the island until reaching the second island
        step = -1
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if grid[i][j] == 1:
                    return step
                for d in dirs:
                    x, y = i+d[0],j+d[1]
                    if x<0 or y<0 or x>=m or y>=n or visited[x][y]:
                        continue
                    visited[x][y] = True
                    queue.append((x,y))
            #increment the step
            step +=1
                    
        return -1
            
                    