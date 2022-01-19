class WordDictionary:

    def __init__(self):
        # use a dictionary to store the key
        self.word_dict = defaultdict(list)

    def addWord(self, word: str) -> None:
        # add the word to the dictionary if the word does not already exist
        word_len = len(word)
        if word not in self.word_dict[word_len]:
            self.word_dict[word_len].append(word)

    def search(self, word: str) -> bool:
        word_len = len(word)
        if word_len not in self.word_dict:
            return False
        for w in self.word_dict[word_len]:
            count = word_len
            for i,c in enumerate(word):
                if c!='.' and w[i]!=c:
                    break
                count -= 1
            if count == 0:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)