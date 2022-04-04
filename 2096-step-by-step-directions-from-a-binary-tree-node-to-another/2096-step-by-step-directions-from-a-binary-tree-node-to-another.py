# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # first use dfs to create a hashmap {node:parent_node}, then build a graph?
        # convert tree to a graph, and then bfs to find shortest path?
        
        nodeMap = defaultdict(list)
        # {node: (parent_node, parent), node: (child_node, left)}
        
        def dfs(root, parent, direction):
            if not root:
                return
            
            # need to use these if statements to determine whether it's a left or right child
            if parent:
                nodeMap[root.val].append((parent.val, 'U'))
                nodeMap[parent.val].append((root.val, direction))
                
            dfs(root.left, root, 'L')
            dfs(root.right, root, 'R')
        
        dfs(root, None, None)
        
#         print(nodeMap)
        
        #bfs to find shortest path. use a tuple (current value, current answer) to track the path
        queue = deque([(startValue, "")])
        visited = set()
        visited.add(startValue)
        
        while queue:
            curVal, curStr = queue.popleft()
            if curVal==destValue:
                return curStr
            # bfs neighbors
            for nxt, relation in nodeMap[curVal]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                queue.append((nxt, curStr+relation))
        
        return ""
                