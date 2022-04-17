class Solution:
    def baseNeg2(self, n: int) -> str:
        if n in [0,1]:
            return str(n)
        
        def dfs(n, cur):
            if n==0:
                return cur
            
            if n%-2==0:
                return dfs(n//-2, "0"+cur)
            else:
                return dfs((n-1)//-2, "1"+cur)
        
        return dfs(n, "")