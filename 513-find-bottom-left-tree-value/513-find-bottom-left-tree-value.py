# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #level-order traversal
        if not root:
            return -1
        
        res = root.val
        queue = deque([root])
        flag = False
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not flag:
                    res = node.val
                    flag = True
                    
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            flag = False
        
        return res
                
                
            
                