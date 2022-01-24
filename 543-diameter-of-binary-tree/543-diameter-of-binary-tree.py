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
            
            diameter = left_h + right_h
            
            self.val = max(self.val, diameter)
            
            return max(left_h, right_h)+1
        
        helper(root)
    
        return self.val