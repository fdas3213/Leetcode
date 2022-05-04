# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(root, low, high):
            if not root:
                return 
            
            if root.val<low:
                return dfs(root.right, low, high)
            elif root.val>high:
                return dfs(root.left, low, high)
            else:
                root.left = dfs(root.left, low, high)
                root.right = dfs(root.right, low, high)
                return root
        
        return dfs(root, low, high)