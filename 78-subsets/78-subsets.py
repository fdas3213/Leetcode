class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start:int, temp:List[int]):
            res.append(list(temp))
            if len(temp)==len(nums):
                return
            
            for i in range(start, len(nums)):
                if i<start:
                    continue
                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.remove(nums[i])
                
        backtrack(0, [])
        
        return res