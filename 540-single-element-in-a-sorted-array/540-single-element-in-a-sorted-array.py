class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            right_even = (right-mid)%2==0
            if nums[mid]==nums[mid+1]:
                if right_even:
                    #after removing nums[mid+1], right side is not even anymore, so should move left pointer to the right of mid+1
                    left = mid +2
                else:
                    right = mid -1
            elif nums[mid]==nums[mid-1]:
                if right_even:
                    right = mid-2
                else:
                    left = mid+1
            else:
                return nums[mid]
        
        return nums[left]