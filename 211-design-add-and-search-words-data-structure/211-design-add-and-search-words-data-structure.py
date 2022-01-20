class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        # use a dictionary to store the key
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
            else:
                current.children[ch] = TrieNode()
                current = current.children[ch]
        current.endOfWord = True
            

    def search(self, word: str) -> bool:
        return self.searchRecursive(self.root, word, 0)
        
    def searchRecursive(self, current, word, index):
        # if index is the last letter of word, check if the current TrieNode is the end of word
        if index == len(word):
            return current.endOfWord
        # if '.', then for every child of current TrieNode, we check if there's a match with any child
        if word[index] == '.':
            for child in current.children:
                if self.searchRecursive(current.children[child], word, index+1):
                    return True
        # if there's a match, go deeper   
        if word[index] in current.children:
            return self.searchRecursive(current.children[word[index]], word, index+1)
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)