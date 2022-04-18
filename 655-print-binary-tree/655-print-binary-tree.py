# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        #width is 2**h-1
        def get_height(root):
            if not root:
                return 0
            left_h = get_height(root.left)
            right_h = get_height(root.right)
            return max(left_h, right_h) + 1
        
        height = get_height(root)
        width = 2**height-1
        res = [['' for _ in range(width)] for _ in range(height)]
        
        def update_node(node, row, left, right):
            if not node:
                return
            mid = left+(right-left)//2
            res[row][mid] = str(node.val)
            update_node(node.left, row+1, left, mid-1)
            update_node(node.right, row+1, mid+1, right)
        
        update_node(root, 0, 0, width)
        
        return res
        
        