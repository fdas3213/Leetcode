class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0
        n = len(prices)
        # dp = [0 for _ in range(n)]
        for i in range(1, n):
            #dp[i] = max(0, prices[i]-minPrice)
            ans = max(ans, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        
        return ans