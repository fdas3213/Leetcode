class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        m, n = len(board), len(board[0])
        
        def inRange(x, y):
            return x>=0 and y>=0 and x<m and y<n
        
        def isValid(x, y):
            if inRange(x,y):
                #if within the range, then the neighbor of the letter can only be #
                #to satisfy condition 3&4
                return board[x][y]=='#'
            #if out of range, that means the letter is at the boundary, so it will not have 
            #any empty cell, and satisfies condition 3&4
            return True
        
        def isPossible(x, y, d):
            i = 0
            while i<len(word) and inRange(x, y) and (board[x][y]==' ' or board[x][y]==word[i]):
                i += 1
                x += d[0]
                y += d[1]
            
            #we break out of the loop before i reaches the last character
            if i<len(word):
                return False
            
            #we need to check if the position of the last character is a valid position
            return isValid(x,y)
        
        def dfs(i:int, j:int):
            #terminal condition 
            if board[i][j]!=' ' and board[i][j] != word[0]:
                return False
            
            for d in dirs:
                x, y = i-d[0], j-d[1]
                #we need to proceed along the current direction. We cannot explore 4 neighboring cells, 
                # we can only explore along the direction of the current neighbor
                if isValid(x,y) and isPossible(i, j, d):
                    return True
            
            return False
        

        for i in range(m):
            for j in range(n):
                if board[i][j]!='#' and dfs(i, j):
                    return True
        
        return False