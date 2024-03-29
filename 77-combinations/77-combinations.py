class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[i+1 for i in range(n)]]
        
        res = []
        
        def dfs(start:int, temp: List[int]):
            # terminal condition    
            if len(temp)==k:
                res.append(list(temp))
                return
            
            for i in range(start, n+1):
                temp.append(i)
                dfs(i+1, temp)
                temp.remove(i)
        
        dfs(1, [])
        
        return res
            