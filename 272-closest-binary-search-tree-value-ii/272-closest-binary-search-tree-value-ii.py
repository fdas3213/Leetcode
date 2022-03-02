# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        #O(N): traverse the tree and update the maxheap to pop the max distance node
        maxHeap = []
        
        def dfs(root):
            if not root:
                return
            dist = abs(target-root.val)
            heappush(maxHeap, (-dist,root.val))
            if len(maxHeap)>k:
                heappop(maxHeap)
            # if target>=root.val:
            #     dfs(root.right)
            # else:
            #     dfs(root.left)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        res = []
        while maxHeap:
            res.append(heappop(maxHeap)[1])
            
        return res
            