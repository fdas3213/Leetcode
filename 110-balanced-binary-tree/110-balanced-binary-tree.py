# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        def helper(root):
            if not root:
                return 0
            left_h = helper(root.left)
            right_h = helper(root.right)
            if left_h==-1 or right_h==-1 or abs(left_h-right_h)>1:
                return -1
            return max(left_h, right_h) + 1
        
        return helper(root) != -1