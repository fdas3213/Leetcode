class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1 = grid[0]
        inverted_r1 = [1-val for val in grid[0]]
        
        for row in range(1, len(grid)):
            if grid[row]!=r1 and grid[row]!=inverted_r1:
                return False
        
        return True