class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [0,-1], [1,0],[-1,0]]
        
        m, n = len(grid), len(grid[0])
        
        # use two matrices to denote (distance sum) and (number of houses that can be reached)
        # from point[i][j]
        distance_matrix = [[0]*n for _ in range(m)]
        house_matrix = [[0]*n for _ in range(m)]
        
        def bfs(i, j):
            visited = set()
            queue = deque([(i,j,0)])
            
            visited.add((i,j))
            
            while queue:
                i, j, dist = queue.popleft()
                # if we start from a building and reached an empty land(grid[i][j]=0),
                # we add the distance and increment the count
                if grid[i][j]==0:
                    distance_matrix[i][j] += dist
                    house_matrix[i][j] += 1
                
                #traverse neighbor cells
                for d in dirs:  
                    x, y = i+d[0], j+d[1]
                    if x<0 or y<0 or x>=m or y>=n or grid[x][y]!=0:
                        continue
                    if (x,y) not in visited:
                        visited.add((x,y))
                        queue.append((x,y, dist+1))
        
        # find all houses
        minDistance = float("inf")
        houseCnt = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    houseCnt += 1
                    bfs(i, j)
                
        
        #check all cells and see if there exists a cell that can be visited from all buildings/houses
        for i in range(m):
            for j in range(n):
                if house_matrix[i][j] == houseCnt:
                    minDistance = min(minDistance, distance_matrix[i][j])

        return minDistance if minDistance!=float("inf") else -1