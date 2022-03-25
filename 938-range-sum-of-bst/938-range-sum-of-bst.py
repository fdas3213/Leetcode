# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        
        def dfs(root):
            if not root:
                return
            
            if root.val>=low and root.val<=high:
                self.ans += root.val
                dfs(root.left)
                dfs(root.right)
            
            if root.val<low:
                #no need to traverse left branch
                dfs(root.right)
            
            if root.val>high:
                #no need to traverse right branch 
                dfs(root.left)
        
        dfs(root)
        return self.ans