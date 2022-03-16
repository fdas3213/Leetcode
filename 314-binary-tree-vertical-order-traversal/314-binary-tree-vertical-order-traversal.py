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
        
        treeMap = defaultdict(list)
        queue = deque([(root, 0)])
        min_l, max_l = 0, 0
        while queue:
            node, level = queue.popleft()
            treeMap[level].append(node.val)
            min_l = min(min_l, level)
            max_l = max(max_l, level)
            
            if node.left:
                queue.append((node.left, level-1))
            
            if node.right:
                queue.append((node.right, level+1))
        
        res = []
        for i in range(min_l, max_l+1):
            res.append(treeMap[i])
        
        return res
        