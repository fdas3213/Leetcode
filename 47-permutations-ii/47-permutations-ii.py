class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        
        def backtrack(temp:List[int]):
            if len(temp)==len(nums):
                res.append(list(temp))
                return
            
            for i in range(len(nums)):
                if (used[i]) or (i>0 and nums[i]==nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                temp.append(nums[i])
                backtrack(temp)
                used[i] = False
                temp.pop()
        
        backtrack([])
        
        return res