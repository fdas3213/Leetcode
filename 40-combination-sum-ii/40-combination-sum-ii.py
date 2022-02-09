class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        
        def backtrack(start: int, cursum: int, temp:List[int]):
            if cursum==0:
                res.append(list(temp))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i]>cursum:
                    continue
                    
                if i>start and candidates[i]==candidates[i-1]:
                    continue

                temp.append(candidates[i])
                backtrack(i+1, cursum-candidates[i], temp)
                temp.pop()
        
        backtrack(0, target, [])
        
        return res