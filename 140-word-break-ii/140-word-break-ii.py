class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        segments = deque([s])
        res = deque([""])
        ans = []
        
        while segments:
            l = len(segments)
            for i in range(l):
                curstr = segments.popleft()
                cur_sol = res.popleft()
                #add solution to the output when segment is empty
                if len(curstr) == 0:
                    ans.append(cur_sol)
                    continue
                for word in wordDict:
                    if curstr.startswith(word):
                        #find the index of word in curstr, and add rest of curstr into segments
                        word_len = len(word)
                        newstr = curstr[word_len:]
                        segments.append(newstr)
                        
                        # add word to the solution
                        new_sol = cur_sol+word
                        if len(newstr)!=0:
                            new_sol += " "
                        res.append(new_sol)
        
        return ans