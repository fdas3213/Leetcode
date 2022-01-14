class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board),len(board[0])
        if m == 0 or n ==0:
            return 0
        
        #step 1. turn all 'O' on the 1st row or last row and those connected to 'P'
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, m, n)
            if board[m-1][j] == 'O':
                self.dfs(board, m-1, j, m, n)
        
        # step 2. turn all 'O' on the 1st column or last column to those connected to 'P'
        for j in range(m):
            if board[j][0] == 'O':
                self.dfs(board, j, 0, m, n)
            if board[j][n-1] == 'O':
                self.dfs(board, j, n-1, m, n)
        
        # step 3. flip all 'O' to X and '*' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'P':
                    board[i][j] = 'O'
    
    def dfs(self, board: List[List[str]], i: int, j: int, m:int, n:int):
        # boundary check
        if i<0 or j<0 or i>=m or j>=n or board[i][j] != 'O':
            return
        
        board[i][j] = 'P'
        
        self.dfs(board, i-1, j,m,n)
        self.dfs(board, i+1, j,m,n)
        self.dfs(board, i, j+1,m,n)
        self.dfs(board, i, j-1,m,n)
        