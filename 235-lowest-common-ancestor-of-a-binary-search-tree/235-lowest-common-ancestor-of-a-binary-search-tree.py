# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        
        """
        Three cases. 
        1. p and q on separate side of the tree 
        2. p and q both on the left side of the root node, then we traverse left tree 
        3. p and q both on the right side of the root node, then we traverse right tree
        """
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            
        return self.lowestCommonAncestor(root, p, q)