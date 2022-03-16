class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def dfs(temp: List[int], i: int):
            num = temp.pop()
            
            #to avoid duplicate
            while i*i<=num:
                div = num/i
                if num%i==0:
                    res.append(temp+[i, div])
                    dfs(temp+[i,div], i)
                i+=1
        
        dfs([n], 2)
        
        return res
            