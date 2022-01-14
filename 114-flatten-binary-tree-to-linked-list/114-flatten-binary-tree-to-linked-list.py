# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        while root:
            r = root.right
            if root.left:
                l = root.left
                while l.right:
                    #find the right most leaf node in the left subtree
                    l = l.right
                l.right = r
                root.right = root.left
                root.left = None
            root = root.right