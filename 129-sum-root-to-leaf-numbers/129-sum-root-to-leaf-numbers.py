# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(root, curSum):
            nonlocal totalSum
            
            if not root:
                return
            curSum = curSum * 10 + root.val
            if not root.left and not root.right:
                #at the leaf node
                totalSum += curSum
            else:
                helper(root.left, curSum)
                helper(root.right, curSum)
        
        totalSum = 0
        helper(root, 0)
        
        return totalSum