# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        
        def helper(root):
            if not root:
                return -1

            left_h = helper(root.left)
            right_h = helper(root.right)

            cur_h = 1 + max(left_h, right_h)

            res[cur_h].append(root.val)
            return cur_h
        
        helper(root)
        return res.values()