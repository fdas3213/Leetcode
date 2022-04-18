class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #two pointers
        
        #sort the input array
        nums.sort()
        
        cnt = 0
        l = len(nums)
        for i in range(l-1, 1, -1):
            left, right = 0, i-1
            
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    cnt += (right-left)
                    right -= 1
                else:
                    left += 1
        
        return cnt