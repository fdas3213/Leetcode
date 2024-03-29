# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        bad_node = []
        
        def recover(root):
            nonlocal pre
            
            if not root:
                return
            
            recover(root.left)
            if pre and pre.val >= root.val:
                bad_node.append((pre, root))
            
            pre = root
            
            recover(root.right)
        
        pre = None
        recover(root)
        temp = bad_node[0][0].val
        bad_node[0][0].val = bad_node[-1][1].val
        bad_node[-1][1].val = temp