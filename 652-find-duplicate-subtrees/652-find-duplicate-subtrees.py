# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # {Node:count}
        nodeMap = defaultdict(int)
        ans = []
        
        def dfs(root):
            if not root:
                return "#"
            
            serial = str(root.val)+","+dfs(root.left)+","+dfs(root.right)
            nodeMap[serial] += 1
            
            if nodeMap[serial]==2:
                #cannot use nodeMa[serial]>1 because duplicate will be added if its count=3,4,5...
                ans.append(root)        
            
            return serial
        
        dfs(root)
        
        return ans