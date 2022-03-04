class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #initialize an adjacency list
        graph = {i:[] for i in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        
        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                count += 1
                visited.add(node)
                self.dfs(node, graph, visited)
        
        return count
    
    def dfs(self, node, graph, visited):    
        # visited[node] = 1
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, graph, visited)