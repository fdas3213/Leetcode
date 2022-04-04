class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        empty = len(moves)!=9
        self.size = 3
        
        playerMoves = [[0 for _ in range(3)] for _ in range(3)]
        
        def checkRow(row, player):
            for i in range(3):
                if playerMoves[row][i] != player:
                    return False
            return True
        
        def checkCol(col, player):
            for i in range(3):
                if playerMoves[i][col] != player:
                    return False
            return True
        
        def checkDiagonal(player):
            for i in range(3):
                if playerMoves[i][i] != player:
                    return False
            return True
        
        def checkAntiDiagonal(player):
            for i in range(3):
                if playerMoves[i][2-i] != player:
                    return False
            return True
        
        for i, (r, c) in enumerate(moves):
            player = 'A' if i%2==0 else 'B'
            playerMoves[r][c] = player
            if checkRow(r, player) or checkCol(c,player) or checkDiagonal(player) or checkAntiDiagonal(player):
                return player
        
        if empty:
            return 'Pending'
        else:
            return 'Draw'