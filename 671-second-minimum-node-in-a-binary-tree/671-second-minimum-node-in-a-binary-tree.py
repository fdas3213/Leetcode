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
        
        # if we reach a node which has value greater than the root node value, then we do not need to go deeper of that node anymore because the child node's value is at least as large as that node
        queue = deque([root])
        smallest, sec = root.val, float("inf")
        while queue:
            root = queue.popleft()
            if root.left:
                if root.left.val > smallest and root.left.val < sec:
                    sec = root.left.val
                if root.left.val == root.val:
                    queue.append(root.left)
                
            if root.right:
                if root.right.val > smallest and root.right.val < sec:
                    sec = root.right.val
                if root.right.val == root.val:
                    queue.append(root.right)
        
        return sec if sec!=float("inf") else -1
            
        
        