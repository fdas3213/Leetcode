# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        self.ans = 0
        
        def helper(root, targetSum):
            if not root:
                return
            
            targetSum -= root.val
            
            if targetSum == 0:
                self.ans += 1
            
            helper(root.left, targetSum)
            helper(root.right, targetSum)
        
        def preorder(root):
            if not root:
                return
            
            helper(root, targetSum)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        
        return self.ans
            
            
                