class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if k>sum(ribbons):
            return 0
        
        def check(ribbon_len:int):
            count = 0
            for ribbon in ribbons:
                count += (ribbon//ribbon_len)
            
            return count>=k
        
        left, right = 1, max(ribbons)
        
        while left<=right:
            mid = left+(right-left)//2
            if check(mid):
                left = mid + 1
            else:
                right = mid-1
        
        return right