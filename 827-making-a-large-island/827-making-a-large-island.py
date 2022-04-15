class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        colorIdx = 2
        islandColor = defaultdict(int)
        
        """
        The idea is to 
        1. add a color "id" to all 1-valued cells, and dfs its neighboring cells
        2. iterate over all 0-valued cells, and dfs its neighbor cells
        """
        def dfs(i, j, color):
            # increment the current color id by 1
            islandColor[color] += 1
            # paint the current cell by the color id
            grid[i][j] = color
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or grid[x][y]!=1:
                    continue
                # add 1 because grid[x][y] is an island
                # the dfs(x,y) to explore neighboring islands of (x,y)
                dfs(x,y,color)
        
        #iterate over 1-valued cells first
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i, j, colorIdx)
                    colorIdx += 1
        
        #all cells are 0
        if not islandColor:
            return 1
        # set ans to be the max area of 1s
        ans = max(islandColor.values())
        
        #iterate over 0-valued cells
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    neighbors = set()
                    for d in dirs:
                        x, y = i+d[0], j+d[1]
                        if x<0 or y<0 or x>=m or y>=n or grid[x][y]==0:
                            continue
                        neighbors.add(grid[x][y])
                    curSize = 1
                    for color in neighbors:
                        curSize += islandColor[color]
                    ans = max(ans, curSize)
        
        return ans
            