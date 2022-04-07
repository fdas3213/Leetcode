# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def get_left_height(root):
            if not root:
                return 0
            return 1 + get_left_height(root.left)
        
        def get_right_height(root):
            if not root:
                return 0
            return 1 + get_right_height(root.right)
        
        left_h = get_left_height(root)
        right_h = get_right_height(root)
        
        if left_h==right_h:
            return 2**left_h - 1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        
        
            