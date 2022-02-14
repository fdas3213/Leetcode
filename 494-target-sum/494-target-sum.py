class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        self.memo = defaultdict(int)
        
        def backtrack(cursum: int, start: int):
            if (start, cursum) in self.memo:
                return self.memo[(start, cursum)]
            if start==len(nums) and cursum==target:
                return 1
            elif start==len(nums):
                return 0
            
            pos = backtrack(cursum+nums[start], start+1)
            neg = backtrack(cursum-nums[start], start+1)
            
            self.memo[(start, cursum)] = pos+neg
            
            return pos+neg
        
        return backtrack(0, 0)