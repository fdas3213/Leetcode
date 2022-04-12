class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        memo_p = set()
        memo_a = set()
        
        def dfs(i:int, j:int, visited):
            if (i,j) in visited:
                return
            
            visited.add((i,j))
            
            for d in dirs:
                x, y = i+d[0],j+d[1]
                if x<0 or y<0 or x>=m or y>=n or heights[x][y]<heights[i][j]:
                    continue
                dfs(x,y,visited)

        res = []
        
        for i in range(m):
            dfs(i, 0, memo_p)
            dfs(i, n-1, memo_a)
        
        for j in range(n):
            dfs(0, j, memo_p)
            dfs(m-1, j, memo_a)
        
        for pos in memo_p:
            if pos in memo_a:
                res.append(pos)
        
        return res