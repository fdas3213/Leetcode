# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        #inorder traversal
        nodes = []
        stack = []
        count = 0
        closest = root.val
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nodes.append(root.val)
            count += 1
            if abs(root.val-target)<abs(closest-target):
                closest = root.val
            root = root.right
        
        closestIndex = 0
        for index, item in enumerate(nodes):
            if item==closest:
                closestIndex = index
        res = [closest]
        left, right = closestIndex-1, closestIndex+1
        while k>1:
            if left>=0 and right<count:
                if abs(nodes[left]-target)<abs(nodes[right]-target):
                    res.append(nodes[left])
                    left -= 1
                else:
                    res.append(nodes[right])
                    right += 1
            elif left>=0:
                res.append(nodes[left])
                left -= 1
            elif right<count:
                res.append(nodes[right])
                right += 1
            
            k-=1
        
        return res
                    
        
        return res
            
        
            
        