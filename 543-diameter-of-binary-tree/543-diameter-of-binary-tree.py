# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.val = 0
        
        def helper(root):
            if not root:
                return 0
            left_h = helper(root.left)
            right_h = helper(root.right)
            
            max_depth = max(left_h, right_h) + 1
            
            return max_depth
        
        def preorder(root):
            if not root:
                return
            max_left = helper(root.left)
            max_right = helper(root.right)
            self.val = max(self.val, max_left+max_right)
            
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        return self.val