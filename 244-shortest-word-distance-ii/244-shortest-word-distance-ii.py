class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordMap = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self.wordMap[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = len(self.wordMap[word1]), len(self.wordMap[word2])
        p1, p2 = 0, 0
        curMin = abs(self.wordMap[word1][p1]-self.wordMap[word2][p2])
        while p1<l1 and p2<l2:
            m1, m2 = self.wordMap[word1][p1], self.wordMap[word2][p2]
            curMin = min(curMin, abs(m1-m2))
            if m1<=m2:
                p1+=1
            else:
                p2+=1
        return curMin
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)