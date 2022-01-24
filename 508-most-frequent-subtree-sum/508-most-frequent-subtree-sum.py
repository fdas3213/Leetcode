# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.max_count = 0
        self.sumMap = defaultdict(int)
        
        def helper(root):
            if not root:
                return 0
            
            leftsum = helper(root.left)
            rightsum = helper(root.right)
            
            cursum = leftsum + rightsum + root.val
            
            self.sumMap[cursum] += 1
            self.max_count = max(self.max_count, self.sumMap[cursum])
            
            return cursum
        
        helper(root)
        res = []
        for k,v in self.sumMap.items():
            if v == self.max_count:
                res.append(k)
        
        return res
        
            
        