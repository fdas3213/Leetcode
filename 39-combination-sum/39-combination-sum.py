class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start:int, temp: List[int], cursum:int):
            if cursum==0:
                res.append(list(temp))
                return
            elif cursum<0:
                return
            
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                backtrack(i, temp, cursum-candidates[i])
                temp.pop()
        
        backtrack(0, [], target)
        
        return res