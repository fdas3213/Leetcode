class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.endOfWord = True
            
    def search(self, word: str) -> bool:
        return self.searchRecursive(self.root, word, 0)
        
    def searchRecursive(self, node, word, index):
        if index == len(word):
            return node.endOfWord
        
        if word[index] in node.children:
            return self.searchRecursive(node.children[word[index]], word, index+1)
        
        return False
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)