class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #edge case
        if endWord not in wordList:
            return 0
        
        #(word, distance)
        queue = deque([(beginWord, 1)])
        remaining = set(wordList)
        
        while queue:
            # print(queue, remaining)
            cur, dist = queue.popleft()
            if cur==endWord:
                return dist
            
            #iterate over every character of the current word
            for i, ch in enumerate(cur):
                for letter in string.ascii_lowercase:
                    nxt = cur[:i]+letter+cur[i+1:]
                    if nxt in remaining:
                        queue.append((nxt, dist+1))
                        remaining.remove(nxt)
        
        return 0