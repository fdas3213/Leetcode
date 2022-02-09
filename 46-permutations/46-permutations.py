class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(temp:List[int]):
            if len(temp)==len(nums):
                res.append(list(temp))
                return
            
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                backtrack(temp)
                temp.pop()
        
        backtrack([])
        
        return res