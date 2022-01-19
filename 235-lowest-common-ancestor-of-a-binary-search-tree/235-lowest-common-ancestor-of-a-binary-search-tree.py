# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        def LCA(root, p, q):
            if not root:
                return
            if p.val == root.val:
                return p
            if q.val == root.val:
                return q
            
            if (p.val < root.val and q.val > root.val) or (p.val>root.val and q.val < root.val):
                return root
            elif p.val < root.val and q.val < root.val:
                return LCA(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return LCA(root.right, p, q)
            
        return LCA(root, p, q)