# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
#         def get_height(root):
#             if not root:
#                 return 0 
#             left_h = get_height(root.left)
#             return 1+left_h
            
        self.ans = 0
        def count(root):
            if not root:
                return
            self.ans += 1
            count(root.left)
            count(root.right)
        
        count(root)
        
        return self.ans
        
            