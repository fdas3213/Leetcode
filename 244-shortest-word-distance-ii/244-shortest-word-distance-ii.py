class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_index = defaultdict(list)
        self.n = 0
        for index, word in enumerate(wordsDict):
            self.word_index[word].append(index)
            self.n += 1
        
    def shortest(self, word1: str, word2: str) -> int:
        w1_list = self.word_index[word1]
        w2_list = self.word_index[word2]
        min_dist = self.n
        if len(w1_list)==len(w2_list)==1:
            return abs(w1_list[0]-w2_list[0])
        
        p1, p2 = 0,0
        while p1<len(w1_list) and p2<len(w2_list):
            #"and" operator is used because when one pointer hits the end, incrementing the other pointer would only create a bigger difference
            min_dist = min(min_dist, abs(w1_list[p1]-w2_list[p2]))
            if w1_list[p1]<w2_list[p2]:
                p1 += 1
            else:
                p2 += 1
        return min_dist
                    

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)