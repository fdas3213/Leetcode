class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # the idea is to use DP or brute force to go over four directions
        
        ans = 0
        dp = defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    # there're 4 directions that we need to track
                    # previous column
                    dp[i,j,0] = dp[i,j-1,0]+1
                    # previous row
                    dp[i,j,1] = dp[i-1,j, 1]+1
                    # diagonal
                    dp[i,j,2] = dp[i-1,j-1,2]+1
                    # anti-diagonal
                    dp[i,j,3] = dp[i-1,j+1,3]+1
                    
                    ans = max(ans, dp[i,j,0], dp[i,j,1], dp[i,j,2], dp[i,j,3])
                    
        return ans