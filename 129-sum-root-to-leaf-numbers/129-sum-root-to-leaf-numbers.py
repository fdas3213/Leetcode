# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(root, cur):
            # terminal condition
            if not root:
                return
            
            if not root.left and not root.right:
                self.ans += cur*10+root.val
                return
            
            dfs(root.left, cur*10+root.val)
            dfs(root.right, cur*10+root.val)
        
        dfs(root, 0)
        
        return self.ans