class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if beginWord==endWord or endWord not in wordList:
            return 0
        
        # bfs
        queue = deque([beginWord])
        letters = list(string.ascii_lowercase)
        wordList = set(wordList)
        count = 1
        
        while queue:
            size = len(queue)
            # for elements in queue that already have "count" number of transformations
            for i in range(size):
                # for each word in the queue
                cur = queue.popleft()
                if cur == endWord:
                    return count
                # for each position of the current word
                for pos, char in enumerate(cur):
                    # for each alphabetic letter
                    for letter in letters:
                        if letter == char:
                            continue
                        newWord = cur[:pos] + letter + cur[pos+1:]
                        if newWord in wordList:
                            wordList.remove(newWord)
                            queue.append(newWord)
            count += 1
        
        return 0
                        
            