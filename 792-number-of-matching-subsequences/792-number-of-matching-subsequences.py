class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordMap = defaultdict(list)
        for word in words:
            wordMap[word[0]].append(word)
        
        count = 0
        
        #iterate over s to save time since length of s is much longer than that of words
        for char in s:
            word_to_check = wordMap[char]
            # reset the character mapping
            wordMap[char] = []
            for word in word_to_check:
                if len(word)==1:
                    count += 1
                else:
                    wordMap[word[1]].append(word[1:])

        return count