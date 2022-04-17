class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A tree is valid if
        1. every node is connected: for every pair of nodes in graph, there is a path between them
        2. there's not a cycle: number of edges==n-1
        """
        # check condition 2
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        visited = set()
        #bfs
        visited.add(0)
        queue = deque([(0, -1)])
        
        while queue:
            cur, parent = queue.popleft()
            for neighbor in graph[cur]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                visited.add(neighbor)
                queue.append((neighbor, cur))
        
        return len(visited)==n
        
        
            #dfs      
#         def dfs(cur, parent):
#             if cur in visited:
#                 return
            
#             visited.add(cur)
            
#             for neighbor in graph[cur]:
#                 if neighbor==parent:
#                     continue
                
#                 if neighbor in visited:
#                     return False
                
#                 res = dfs(neighbor, cur)
#                 if not res:
#                     return False
            
#             return True
        
#         return dfs(0, -1) and len(visited)==n
     