class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        segments = deque([(s, "")])
        ans = []
        
        while segments:
            l = len(segments)
            for i in range(l):
                curstr, cursol = segments.popleft()
                #add solution to the output when segment is empty
                if len(curstr) == 0:
                    ans.append(cursol)
                    continue
                for word in wordDict:
                    if curstr.startswith(word):
                        #find the index of word in curstr, and add rest of curstr into segments
                        word_len = len(word)
                        newstr = curstr[word_len:]
                        
                        # add word to the solution
                        new_sol = cursol+word
                        if len(newstr)!=0:
                            new_sol += " "
                            
                        segments.append((newstr, new_sol))
        
        return ans