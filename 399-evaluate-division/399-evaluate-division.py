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
                val = product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    val = evaluate(neighbor, target_node, product*value, visited)
                    if val != -1:
                        break
            visited.remove(cur_node)
            return val
            
        #step 2. evaluate the query
        res = []
        for n1,n2 in queries:
            #if either of the node does not exist in the graph
            if n1 not in graph or n2 not in graph:
                res.append(-1)
            #if n1 and n2 is the same node
            elif n1 == n2:
                res.append(1)
            else:
                visited = set()
                res.append(evaluate(n1, n2, 1, visited))
        
        return res
            
                    