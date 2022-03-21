class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        #initialize the dictionary
        wordMap = defaultdict(list)
        count = 0
        for index, word in enumerate(wordsDict):
            wordMap[word].append(index)
            count += 1
        
        w1_list, w2_list = wordMap[word1], wordMap[word2]
        p1, p2 = 0, 0
        
        curMin = count
        while p1<len(w1_list) and p2<len(w2_list):
            m1, m2 = w1_list[p1], w2_list[p2]
            curMin = min(curMin, abs(m1-m2))
            if m1<m2:
                p1 += 1
            else:
                p2 += 1
        
        return curMin
            
        
        