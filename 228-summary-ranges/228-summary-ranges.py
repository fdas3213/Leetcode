class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #sliding window: O(N)
        ans = []
        
        if not nums:
            return ans
        
        start = 0
        for end in range(1, len(nums)):
            if nums[end]-nums[end-1]!=1:
                if start==end-1:
                    ans.append(f"{nums[start]}")
                else:
                    ans.append(f"{nums[start]}->{nums[end-1]}")
                start = end
        
        #add the last one
        if start==len(nums)-1:
            ans.append(f"{nums[start]}")
        else:
            ans.append(f"{nums[start]}->{nums[len(nums)-1]}")
        
        return ans
            