class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def dfs(temp, i):
            # pop the last element
            n = temp.pop()
            
            while i*i<=n:
                if n%i==0:
                    div = n//i
                    res.append(temp+[i, div])
                    dfs(temp+[i,div], i)
                i += 1
        
        dfs([n], 2)
        
        return res