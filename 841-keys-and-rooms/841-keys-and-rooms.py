class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n_rooms = len(rooms)
        visited = set()
        
        #build a graph:
        graph = defaultdict(list)
        for i, keys in enumerate(rooms):
            for key in keys:
                graph[i].append(key)
                
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        visited.add(0)
        dfs(0)
        
        return len(visited) == n_rooms