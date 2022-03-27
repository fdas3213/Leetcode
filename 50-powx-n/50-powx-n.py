class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            #base case
            if n==0:
                return 1
            half = helper(x, n//2)            
            if n%2==0:
                return half*half
            else:
                return x*half*half
        
        return helper(x,n) if n>=0 else 1/helper(x, -n)