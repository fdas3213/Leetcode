class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums)-1
        while start < end:
            mid = start + (end-start)//2
            count = sum(n<=mid for n in nums)
            
            if count<=mid:
                start = mid+1
            else:
                end = mid
        
        return start