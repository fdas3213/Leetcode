class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        prev_two, prev_one = 0, 1
        
        for i in range(2, n+1):
            cur = prev_two+prev_one
            prev_two = prev_one
            prev_one = cur
        
        return prev_one