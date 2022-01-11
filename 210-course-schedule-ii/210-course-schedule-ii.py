class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # edge case
        if numCourses == 0:
            return []
        
        # initialize the graph
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        
        # build the graph
        for pair in prerequisites:
            c1, c2 = pair[0], pair[1]
            graph[c2].append(c1)
            indegree[c1] += 1
        
        # bfs
        res = []
        queue = deque()
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        # traverse the graph
        while queue:
            c = queue.popleft()
            res.append(c)
            for child in graph[c]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return [] if len(res) != numCourses else res
            