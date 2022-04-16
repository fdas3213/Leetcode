class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxVal, minVal = max(nums), min(nums)
        if maxVal==minVal:
            return minVal
        
        def gcd(a:int, b:int):
            while a:
                a, b = b%a, a
            return b
        
        return gcd(minVal, maxVal)