class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        
        start, end = 0, len(nums)-1
        
        while start<=end:
            mid = start+(end-start)//2
            if target<nums[mid]:
                end=mid-1
            elif target>nums[mid]:
                start=mid+1
            else:
                left, right = mid, mid
                while left>=0 and nums[left]==target:
                    left-=1
                while right<len(nums) and nums[right]==target:
                    right+=1
                return [left+1,right-1]
        
        
        return [-1,-1]
                