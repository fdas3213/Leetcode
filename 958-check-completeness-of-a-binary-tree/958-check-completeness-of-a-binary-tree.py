# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #level or traversal 
        if not root:
            return True
        
        """
        For a complete Binary tree, there should not be any node after the first empty node because
        it either violates
        1. subtrees are not placed as left as possible
        2. some nodes above the last level are missing
        """
        
        cnt = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            
            for i in range(size):
                root = queue.popleft()
                if not root:
                    cnt += 1
                    continue
                elif cnt>0:
                    return False
                    
                queue.append(root.left)
                queue.append(root.right)
            
        return True
        