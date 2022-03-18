class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        """
        Property: two coordinates belong to the same diagonal if r1-c1==r2-c2
        """
        groups = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if i-j not in groups:
                    groups[i-j] = matrix[i][j]
                elif groups[i-j] != matrix[i][j]:
                    return False
        
        return True