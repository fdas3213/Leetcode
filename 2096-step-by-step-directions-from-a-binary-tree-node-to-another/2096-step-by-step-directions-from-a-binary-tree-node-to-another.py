# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #build a graph
        graph = defaultdict(list)
        
        def dfs(parent, root, direction):
            if not root:
                return
            
            if parent:
                graph[root.val].append((parent.val, 'U'))
                graph[parent.val].append((root.val, direction))
                
            dfs(root, root.left, 'L')
            dfs(root, root.right, 'R')
        
        dfs(None, root, 'None')
        
        #bfs to find shortest path
        queue = deque([(startValue, "")])
        visited = set()
        
        while queue:
            cur, curPath = queue.popleft()
            if cur==destValue:
                return curPath
            for neighbor, direction in graph[cur]:
                if neighbor in visited:
                    continue
                
                queue.append((neighbor, curPath+direction))
                visited.add(neighbor)
        
        return ""
                
            