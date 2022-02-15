class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    
        res = []
        
        def dfs(curstr: str, outstr: str):
            #terminal condition
            if len(curstr)==0:
                res.append(outstr)
                return
            
            for word in wordDict:
                if curstr.startswith(word):
                    l = len(word)
                    newstr = curstr[l:]
                    
                    newout = outstr + word
                    if len(newstr)!=0:
                        newout += " "
                    
                    dfs(newstr, newout)
        
        dfs(s, "")
        
        return res