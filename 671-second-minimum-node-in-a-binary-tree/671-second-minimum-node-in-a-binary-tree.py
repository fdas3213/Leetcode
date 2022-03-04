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
        
        nodes = set()
        
        def dfs(root):
            if not root:
                return
            nodes.add(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        smallest, sec = root.val, float("inf")
        for v in nodes:
            if smallest<v<sec:
                sec = v
        
        return sec if sec!=float("inf") else -1
            
        
        