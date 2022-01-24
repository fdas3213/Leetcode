class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if len(board)==0 or len(board[0])==0:
            return []
        
        #rule 1. if a mine is revealed, change it to 'X', end the game
        i, j = click[0],click[1]
        if board[i][j]=='M':
            board[i][j]='X'
            return board
        
        #dirs has 8 directions according to this problem
        def dfs(board, i, j, dirs):
            m, n = len(board), len(board[0])

            #works as visited
            if board[i][j] != 'E':
                return
            
            #rule 2&3. empty square 'E'
            count = 0
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if 0<=x<m and 0<=y<n and board[x][y]=='M':
                    count += 1
            
            if count == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(count)
                return
            
            for d in dirs:
                x, y = i+d[0], j+d[1]
                if 0<=x<m and 0<=y<n:
                    dfs(board, x, y, dirs)
            

        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        
        dfs(board, i,j, dirs)
        
        return board
                        
            