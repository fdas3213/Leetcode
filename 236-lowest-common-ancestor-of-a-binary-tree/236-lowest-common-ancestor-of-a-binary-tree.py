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
            
            if root==p or root==q:
                return root
            
            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)
            
            if left and right:
                return root
            elif left:
                # if just returns one value, that means the other node is nested under the returned node
                return left
            elif right:
                return right
        
        return LCA(root, p, q)
        