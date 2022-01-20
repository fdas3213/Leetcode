class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #initialize an adjacency list
        graph = {i:[] for i in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        
        visited = {node: 0 for node in graph}
        count = 0
        for node in graph:
            if visited[node]==0:
                count += 1
                visited[node] = 1
                self.dfs(node, graph, visited)
        
        return count
    
    def dfs(self, node, graph, visited):    
        # visited[node] = 1
        
        for neighbor in graph[node]:
            if visited[neighbor]==0:
                visited[neighbor] = 1
                self.dfs(neighbor, graph, visited)