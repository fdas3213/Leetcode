class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # {word: list of indices}
        self.wordDict = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self.wordDict[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        w1_list = self.wordDict[word1]
        w2_list = self.wordDict[word2]
        # two pointers approach
        p1, p2 = 0, 0
        l1, l2 = len(w1_list), len(w2_list)
        ans = float('inf')
        while p1<l1 and p2<l2:
            idx1 = w1_list[p1]
            idx2 = w2_list[p2] 

            ans = min(ans, abs(idx1-idx2))
            if ans==1:
                return ans
            
            if idx1<idx2:
                p1 += 1
            else:
                p2 += 1
                
        return ans
           

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)