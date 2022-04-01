class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        prev_one, prev_two = 2, 1
        for i in range(2, n):
            cur = prev_one+prev_two
            prev_two = prev_one
            prev_one = cur
        
        return prev_one