# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        temp, pre, nxt = None, None, None
        while root:
            # next node is the left node
            nxt = root.left
            
            root.left = temp
            temp = root.right
            
            root.right = pre
            pre = root
            
            root = nxt
            
        return pre