class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        step 1. sort the input array by word length
        step 2. for each word, remove one character at a time, and see if the 
        new word exists in the hashmap or not; if it exists, check it's previous sequence length
        """
        wordMap=defaultdict(list)
        
        words.sort(key=lambda x: len(x))
        ans = 1
        for word in words:
            curLen = 1
            l = len(word)
            for i in range(l):
                newWord = word[:i] + word[i+1:]
                prevLen = wordMap.get(newWord, 0)
                curLen = max(curLen, prevLen+1)
            
            wordMap[word] = curLen
            ans = max(ans, curLen)
        
        return ans