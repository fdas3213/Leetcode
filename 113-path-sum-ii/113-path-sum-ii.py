# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        def pathSumHelper(root: TreeNode, targetSum:int, allPaths: List[List[int]], curPath: List[int]): 
            if not root:
                return
            
            # add the current node to the path
            curPath.append(root.val)
            
            #if at leaf node and we find a path, then add the current path to solution
            if not root.left and not root.right and root.val==targetSum:
                allPaths.append(list(curPath))
            else:
                #traverse left and right subtree
                pathSumHelper(root.left, targetSum-root.val, allPaths, curPath)
                pathSumHelper(root.right, targetSum-root.val, allPaths, curPath)
            
            #delete the last node
            del curPath[-1]
        
        res = []
        pathSumHelper(root, targetSum, res, [])
        
        return res