# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        
        self.helper(root)
        
        return self.res
        
    def helper(self, root):
        if not root:
            return -1
        
        left_h = self.helper(root.left)
        right_h = self.helper(root.right)
        
        cur_h = 1 + max(left_h, right_h)
        if len(self.res) == cur_h:
            self.res.append([])
        
        self.res[cur_h].append(root.val)
        
        return cur_h