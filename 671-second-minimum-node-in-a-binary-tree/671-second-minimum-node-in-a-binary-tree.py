# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return -1
        
        min1, self.min2 = root.val, float("inf")
        
        def dfs(root):
            if not root:
                return

            if root.val > min1 and root.val<self.min2:
                self.min2 = root.val
            
            if root.val == min1:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        
        return self.min2 if self.min2!=float("inf") else -1
            
        
        