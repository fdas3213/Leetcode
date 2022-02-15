class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        #building a trienode
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.endOfWord = True
        node.word = word

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #four directions to search
        self.num_words = len(words)
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        root = trie.root
        
        #memoization
        m, n = len(board), len(board[0])
        res = []
        
        def backtrack(i:int,j:int, parent:TrieNode):
            if self.num_words==0:
                #no need to proceed
                return
            
            #adding the word to result if found
            if parent.endOfWord:
                res.append(parent.word)
                #dedup
                parent.endOfWord = False
                self.num_words -=1 
                
            #terminal condition 2
            if i<0 or j<0 or i>=m or j>=n or board[i][j] not in parent.children:
                return
        
            #memoization to optimize
            ch = board[i][j]
            board[i][j] = "#"
            
            for d in [[-1,0],[1,0],[0,-1],[0,1]]:
                x = i+d[0]
                y = j+d[1]
                backtrack(x, y, parent.children[ch])
            
            board[i][j] = ch
            
        # Word Search
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    backtrack(i, j, root)
            
        return res
            
            
                
            

       