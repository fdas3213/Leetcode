# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        
        pre, temp = None, None
        
        while root:
            n = root.left
            #swap nodes
            root.left = temp
            temp = root.right
            root.right = pre
            pre = root
            
            root = n
        
        return pre
            
            
            
            