class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        used = set()
        
        def dfs(cur:str):
            # terminal condition: the input has been completely segmented 
            if cur=="":
                return True
            
            for word in wordDict:
                if cur.find(word)==0:
                    nxt = cur[len(word):]
                    if nxt not in used:
                        used.add(nxt)
                        if dfs(nxt):
                            return True
            
            return False
        
        return dfs(s)