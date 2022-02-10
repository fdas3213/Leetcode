class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [-1 for _ in range(n)]
        #the index of board represents a row, and the value at each index represents the column
        res = []
        
        def isValid(row):
            # check if the board is valid
            for i in range(row):
                # not the same column: board[i] != board[row]
                # not diagonal: board[i]-i == board[row]-row
                if board[i]==board[row]: 
                    return False
                if abs(board[i]-board[row])==abs(i-row):
                    return False
            return True

        def makeboard(valid_board):
            res = []
            for row, column in enumerate(valid_board):
                cur = "."*column+"Q"+"."*(n-1-column)
                res.append(cur)
            return res
    
        
        def dfs(row):
            if row==n:
                res.append(list(board))
                return
            
            for i in range(n):
                board[row]=i
                if isValid(row):
                    dfs(row+1)
        
        dfs(0)
        
        answer = []
        for val_res in res:
            answer.append(makeboard(val_res))
        
        return answer
            
        
    
            
            
            