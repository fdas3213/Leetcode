# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        #levelorder traversal that starts from {0:root}, -1 while traversing left, and +1 while traversing right node
        queue = deque([(root, 0)])
        nodeMap = defaultdict(list)
        curmin, curmax = 0, 0
        while queue:
            node, column = queue.popleft()
            curmin = min(curmin, column)
            curmax = max(curmax, column)
            nodeMap[column].append(node.val)
            
            if node.left:
                queue.append((node.left, column-1))
            if node.right:
                queue.append((node.right, column+1))
        
        res = []
        
        for i in range(curmin, curmax+1, 1):
            res.append(nodeMap[i])
        
        return res
            
            