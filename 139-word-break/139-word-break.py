class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([s])
        used = set()
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                for word in wordDict:
                    if word==cur:
                        return True
                    if cur.find(word)==0:
                        nxt = cur[len(word):]
                        if nxt not in used:
                            used.add(nxt)
                            queue.append(nxt)
                    # if cur.find(word) != -1:
                    #     index = cur.find(word)
                    #     nxt = cur[:index]+cur[index+len(word):]
                    #     queue.append(nxt)
        
        return False