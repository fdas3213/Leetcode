# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        pre = None
        if not root:
            return res
        stack = []
        max_count, cur_count = 0, 0
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            cur_count = 1 if root.val!=pre else cur_count+1
            
            if cur_count == max_count:
                res.append(root.val)
            elif cur_count > max_count:
                res = [root.val]
                max_count = cur_count
            
            pre = root.val
            root = root.right
            
        return res
                
                