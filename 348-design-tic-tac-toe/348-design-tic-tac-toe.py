class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        #mark player's id on the board

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self.check_row(row, player) or self.check_col(col, player) or self.check_diagonal(player) or self.check_anti_diagonal(player):
            return player
        return 0
    
    
    def check_row(self, row, player):
        for col in range(0, self.size):
            if self.board[row][col] != player:
                return False
        return True
        
    def check_col(self, col, player):
        for row in range(0, self.size):
            if self.board[row][col] != player:
                return False
        return True
    
    def check_diagonal(self, player):
        for row in range(0, self.size):
            if self.board[row][row] != player:
                return False
        return True
    
    def check_anti_diagonal(self, player):
        #[0,2], [1,1], [2,0]. row = size-col-1
        for row in range(0, self.size):
            if self.board[row][self.size-row-1] != player:
                return False
        return True

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)