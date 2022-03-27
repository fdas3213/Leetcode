# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #difference btw this problem and LCA I is that we need to traverse over the entire tree
        #to determine whether a node exists or not
        visited = set()
        
        def dfs(root, p, q):
            if not root:
                return root
        
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q) 
            
            if root == p or root == q:
                visited.add(root)
                return root
            
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
        
        lca = dfs(root, p, q)
        return lca if len(visited)==2 else None
            