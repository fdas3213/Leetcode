# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 1
        
        def dfs(parent, child, count):
            self.ans = max(self.ans, count)
            
            # pre-order traversal
            if not child:
                return 
            
            if parent and parent.val+1==child.val:
                dfs(child, child.left, count+1)
                dfs(child, child.right, count+1)
            else:
                dfs(child, child.left, 1)
                dfs(child, child.right, 1)
        
        dfs(None, root, 1)
        
        return self.ans
            