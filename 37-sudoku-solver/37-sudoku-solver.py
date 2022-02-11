class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        
        def isValid(num, row, col):
            # check if this number exists in the row
            # check if this number exists in the column
            # check if this number exists in the 3x3 sub-box
            # identify the box id of the sub-box
            #[[0,1,2],[3,4,5],[6,7,8]]
            box_id = row//3*3 + col//3
            if num in rows[row] or num in cols[col] or num in box[box_id]:
                return False
            
            return True
        
        def backtrack(r, c):
            if r==8 and c==9:
                return True
            elif c==9:
                c = 0
                r += 1
                
            #if current box already filled
            if board[r][c] != '.':
                # go to the right cell
                return backtrack(r, c+1)
            else:
                box_id = (r//3)*3+c//3
                for n in range(1,10):
                    if not isValid(n,r,c):
                        continue
                    board[r][c] = str(n)
                    rows[r].add(n)
                    cols[c].add(n)
                    box[box_id].add(n)
                    
                    if backtrack(r, c+1):
                        return True
                    
                    # backtrack
                    board[r][c] = '.'
                    rows[r].remove(n)
                    cols[c].remove(n)
                    box[box_id].remove(n)
            
            return False
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    v = int(board[i][j])
                    box_id = (i//3)*3+j//3
                    rows[i].add(v)
                    cols[j].add(v)
                    box[box_id].add(v)
        
        backtrack(0,0)
                    