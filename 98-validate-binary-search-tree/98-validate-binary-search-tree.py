# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.validBST(root, float('-inf'), float('inf'))
        
    def validBST(self, root, left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.validBST(root.left, left, root.val) and self.validBST(root.right, root.val, right)