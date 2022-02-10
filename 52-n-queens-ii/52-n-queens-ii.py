class Solution:
    def totalNQueens(self, n: int) -> int:
        if n<=1:
            return n
        
        self.count = 0
        board = [-1 for _ in range(n)]
        
        
        def isValid(row):
            for prev_r in range(row):
                if board[prev_r]==board[row]:
                    return False
                if abs(board[row]-board[prev_r])==abs(row-prev_r):
                    return False
            return True
        
        def dfs(row):
            #terminal condition
            if row==n:
                self.count += 1
                return
            
            for col in range(n):
                board[row] = col
                if isValid(row):
                    dfs(row+1)
        
        dfs(0)
        
        return self.count