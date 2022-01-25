class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target>nums[-1] or target<nums[0]:
            return [-1,-1]
        
        def bisect_left(nums, target):
            start, end = 0, len(nums)-1
            while start < end:
                mid = start + (end-start)//2
                if nums[mid] < target:
                    start = mid +1
                else:
                    end = mid
            return start if nums[start]==target else -1
        
        def bisect_right(nums, target):
            start, end = 0, len(nums)-1
            while start < end:
                mid = start + (end-start)//2+1
                if nums[mid] > target:
                    end = mid -1
                else:
                    start = mid
            return start if nums[start]==target else -1
        
        return [bisect_left(nums,target), bisect_right(nums, target)]