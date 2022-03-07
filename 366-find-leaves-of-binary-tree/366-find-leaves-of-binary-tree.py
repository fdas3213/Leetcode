# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## add a level
        nodeMap = defaultdict(list)
        
        def dfs(root):
            # post-order traversal
            if not root:
                return -1

            left_h = dfs(root.left)
            right_h = dfs(root.right)

            height = max(left_h, right_h) + 1
            nodeMap[height].append(root.val)
            return height
        
        dfs(root)
        
        return nodeMap.values()
            
            
            
            