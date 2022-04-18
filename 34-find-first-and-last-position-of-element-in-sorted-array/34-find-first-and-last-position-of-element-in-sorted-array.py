class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or target<nums[0] or target>nums[-1]:
            return [-1, -1]
        
        def findFirst(nums, target):
            left, right = 0, len(nums)-1
            while left<right:
                mid = left+(right-left)//2
                if nums[mid]<target:
                    left = mid+1
                else:
                    right = mid
            
            return left if nums[left]==target else -1
        
        def findLast(nums, target):
            left, right = 0, len(nums)-1
            while left<right:
                mid = left+(right-left)//2+1
                if nums[mid]>target:
                    right = mid-1
                else:
                    left = mid
            
            return right if nums[right]==target else -1
        
        return [findFirst(nums, target), findLast(nums, target)]
                
                