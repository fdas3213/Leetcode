class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start:int, temp:List[int]):
            if temp in res:
                return
            res.append(list(temp))
            
            for i in range(start, len(nums)):
                if i>0 and nums[i]==nums[i-1] and nums[i] not in temp:
                    continue
                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.remove(nums[i])
        
        backtrack(0, [])
        
        return res