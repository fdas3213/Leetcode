# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
            return -1
        
        self.curMin = float("inf")
        
        def dfs(root, smallest):
            if not root:
                return
            if root.val>smallest:
                self.curMin = min(self.curMin, root.val)
            
            if root.val==smallest:
                dfs(root.left, smallest)
                dfs(root.right, smallest)

        dfs(root, root.val)
        return self.curMin if self.curMin!=float("inf") else -1
            
        
            