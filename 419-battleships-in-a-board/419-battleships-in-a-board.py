class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        m, n = len(board), len(board[0])
        
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(i, j):
            #mark X as # so that it would not be double counted
            board[i][j] = '#'
            
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if x<0 or y<0 or x>=m or y>=n or board[x][y]!='X':
                    continue
                dfs(x,y)
        
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    cnt += 1
                    dfs(i,j)
        
        return cnt