# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        if not root:
            return 0
        
        stack = []
        nsmallest = 0
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nsmallest += 1
            if nsmallest == k:
                return root.val
            pre = root
            root = root.right
        
        return pre.val