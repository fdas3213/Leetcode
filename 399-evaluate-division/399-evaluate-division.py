class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #step 1. initialize a graph
        graph = defaultdict(defaultdict)
        for pair, value in zip(equations, values):
            v1, v2 = pair[0], pair[1]
            graph[v1][v2] = value
            graph[v2][v1] = 1/value
 
        
        def evaluate(cur_node, target_node, product, visited):
            visited.add(cur_node)
            val = -1
            
            neighbors = graph[cur_node]
            
            if target_node in neighbors:
                return product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor not in visited:
                        val = evaluate(neighbor, target_node, product*value, visited)
                    if val != -1:
                        break
            visited.remove(cur_node)
            return val
        
        def evaluate_bfs(cur_node, target_node):
            visited = set()
            queue = deque([(cur_node, 1)])
            while queue:
                cur_node, cur_val = queue.popleft()
                visited.add(cur_node)
                if target_node == cur_node:
                    return cur_val 
                
                neighbors = graph[cur_node]
                
                for neighbor, val in neighbors.items():
                    if neighbor not in visited:
                        queue.append((neighbor, cur_val*val))
            return -1
            
        #step 2. evaluate the query
        res = []
        for n1,n2 in queries:
            #if either of the node does not exist in the graph
            if n1 not in graph or n2 not in graph:
                res.append(-1)
                continue
            #if n1 and n2 is the same node
            if n1 == n2:
                res.append(1)
                continue
            
            #dfs
            visited = set()
            res.append(evaluate(n1, n2, 1, visited))
            #bfs: res.append(evaluate_bfs(n1, n2))
        
        return res
            
                    