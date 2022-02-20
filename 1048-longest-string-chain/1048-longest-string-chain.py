class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        strMap = {}
        maxWordSeq = 1
        
        for word in words:
            curLen = 1
            for i in range(len(word)):
                nextWord = word[:i] + word[i+1:]
                prevLen = strMap.get(nextWord, 0)
                curLen = max(curLen, prevLen+1)
                
            strMap[word] = curLen
            maxWordSeq = max(maxWordSeq, curLen)
        
        return maxWordSeq
                
            
            
            
            