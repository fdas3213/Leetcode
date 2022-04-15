# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        
        def dfs(pre, root):
            if not root:
                return
            if pre and root.val != pre.val:
                self.ans = min(self.ans, root.val)
            
            dfs(root, root.left)
            dfs(root, root.right)
        
        dfs(None, root)
        
        return self.ans if self.ans!=float('inf') else -1