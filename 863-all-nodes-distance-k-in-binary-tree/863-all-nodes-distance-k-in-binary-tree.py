# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #convert tree to graph and the dfs/bfs
        graph = defaultdict(list)
        
        def preorder(root):
            if not root or (not root.left and not root.right):
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
            
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)

        queue = deque([(target.val, 0)])
        visited = set()
        visited.add(target.val)
        ans = []
        while queue:
            cur, dist = queue.popleft()
            if dist==k:
                ans.append(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    queue.append((neighbor, dist+1))
                    visited.add(neighbor)
        
        return ans