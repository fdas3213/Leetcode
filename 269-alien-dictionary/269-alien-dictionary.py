class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # edge case
        if not words or len(words) == 0:
            return ""
        
        # initialize graph and indegree
        graph = defaultdict(list)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = indegree.get(c, 0)
        
        # build the graph
        for i in range(len(words)-1):
            cur, n = words[i], words[i+1]
            min_len = min(len(cur), len(n))
            flag = len(cur) > len(n)
            for j in range(min_len):
                c1, c2 = cur[j], n[j]
                if c1 != c2:
                    graph[c1].append(c2)
                    indegree[c2] = indegree.get(c2, 0) + 1
                    break
                elif j==min_len-1 and flag:
                    return ""
        
        # bfs
        queue = deque()
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        # cyclic graph
        res = ""
        if len(queue) == 0:
            return res
        
        # traverse the graph
        while queue:
            c = queue.popleft()
            res += c
            for child in graph[c]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return "" if len(res)!=len(indegree) else res