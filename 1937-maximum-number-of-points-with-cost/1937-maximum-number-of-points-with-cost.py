class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
        
#         dp[0] = points[0]
#         ans = max(dp[0])
        #no need for 2-D dp array because we only need to retrieve result from the previous row
        dp = [points[0][c] for c in range(n)]
        ans = max(dp)
        
        for r in range(1, m):
            """
            maxGain[i][j] = points[i][j]+max(dp[i-1][k]-abs(j-k)) for 0<=k<=n-1
            if k<j, points[i][j]+dp[i-1][k]-(j-k)=points[i][j]-j + max(dp[i-1][k]+k)
            Because we iterate each column from 0 to n, we only need to consider the case k<j, 
            therefore, at each point (i,j), because points[i][j]-j is fixed, we only need to track
            maxLeftGain[i][j] = max(maxLeftGain[i][j-1], LeftGain[i][j])
                              = max(maxLeftGain[i][j-1], dp[i-1][j]+j)
                              
            if k>j, points[i][j]+max(dp[i-1][k]-(k-j))=points[i][j]+j + max(dp[i-1][k]-k),
            similarly on the right side, we have this recurrrence relationship
            maxRightGain[i][j] = max(maxRightGain[i][j+1], rightGain[i][j])
                               = max(maxRightGain[i][j+1], dp[i-1][j]-j))
            """
            # initialize the maxLeftGain to be dp[r-1][0]
            #leftGain = [dp[r-1][0]] + [0 for _ in range(n-1)]
            leftGain = [dp[0]] + [0 for _ in range(n-1)]
            for k in range(1, n):
                leftGain[k] = max(leftGain[k-1], dp[k]+k) #dp[r-1][k]+k)
            
            # initialize the maxRightGain to be dp[r-1][-1]
            #rightGain = [0 for _ in range(n-1)] + [dp[r-1][-1]-n+1]
            rightGain = [0 for _ in range(n-1)] + [dp[-1]-n+1]
            for k in range(n-2,-1,-1):
                rightGain[k] = max(rightGain[k+1], dp[k]-k)
            
            # update current value and dp array
            nxt = [0 for _ in range(n)]
            for c in range(n):
                nxt[c] = points[r][c] + max(leftGain[c]-c, rightGain[c]+c)
                ans = max(ans, nxt[c])
            
            dp = nxt
        
        return ans