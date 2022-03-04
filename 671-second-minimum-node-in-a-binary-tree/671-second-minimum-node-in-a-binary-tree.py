# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return -1
        
        # we just need to find one child node that has a different value than the parent node, and return the child node
        # child node always has a value greater than its parent node
        queue = deque([root])
        smallest, sec = root.val, float("inf")
        while queue:
            root = queue.popleft()
            if root.left:
                if root.left.val > smallest and root.left.val < sec:
                    sec = root.left.val
                queue.append(root.left)
                
            if root.right:
                if root.right.val > smallest and root.right.val < sec:
                    sec = root.right.val
                queue.append(root.right)
        
        return sec if sec!=float("inf") else -1
            
        
        