class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start:int, temp:List[int]):
            res.append(list(temp))
            
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.pop()
        
        backtrack(0, [])
        
        return res