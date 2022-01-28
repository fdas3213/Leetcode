class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        temp = [0 for _ in range(l)]
        size = 0
        for n in nums:
            left, right = 0, size
            while left < right:
                mid = left+(right-left)//2
                if n>temp[mid]:
                    left=mid+1
                else:
                    right = mid
            temp[left] = n
            size = max(left+1, size)
        
        return size