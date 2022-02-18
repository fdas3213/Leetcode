class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        strMap = {}
        self.res = 0
        
        def dfs(count:int, curstr:str):
            # terminal condition
            if len(curstr)==0:
                return
            
            if curstr in strMap:
                return strMap[curstr]
            
            for j in range(len(curstr)):
                nextstr = curstr[:j] + curstr[j+1:]
                if nextstr in words:
                    dfs(count+1, nextstr)
            
            strMap[curstr] = count
            
            self.res = max(self.res, count)
        
        for word in words[::-1]:
            dfs(1, word)
            
        return self.res
            
            
            
            