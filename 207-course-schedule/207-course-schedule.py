class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        graph = defaultdict(list)
        
        # build the graph
        for pair in prerequisites:
            c1, c2 = pair[0], pair[1]
            graph[c1].append(c2)
            indegree[c2] += 1
        
        # use bfs
        queue = deque()
        # add elements that have indegree=0 to the queue
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        # traverse the graph
        courses = list()
        while queue:
            course = queue.popleft()
            courses.append(course)
            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return len(courses) == numCourses
        
        