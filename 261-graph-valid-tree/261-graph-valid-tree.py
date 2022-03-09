class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A tree is valid if
        1. fully connected: there's a path between every pair of nodes
        2. does not have a cycle: there's exactly one path between each pair of nodes
        """
        if len(edges)!=n-1:
            return False
        #build graph
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # used set to track fully connect, and parent set to track cycle
        used = set()
        used.add(0)
        
        def dfs(node, parent):
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in used:
                    return False
                if neighbor not in used:
                    used.add(neighbor)
                    if not dfs(neighbor, node):
                        return False
            return True

        return dfs(0, -1) and len(used)==n
        
        