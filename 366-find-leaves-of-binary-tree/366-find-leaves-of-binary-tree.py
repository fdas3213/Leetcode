# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        nodeMap = defaultdict(list)
        
        def dfs(root):
            if not root:
                return 0
            
            left_h = dfs(root.left)
            right_h = dfs(root.right)
            
            cur_h = max(left_h, right_h) + 1
            nodeMap[cur_h].append(root.val)
            
            return cur_h
        
        dfs(root)
        
        return list(nodeMap.values())