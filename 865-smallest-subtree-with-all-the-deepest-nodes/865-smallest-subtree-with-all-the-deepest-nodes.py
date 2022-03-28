# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #{node: (parent, depth)}
        nodeMap = {None:-1}
        self.maxDepth = 0
        def dfs(root, parent):
            if not root:
                return
           
            nodeMap[root] = nodeMap[parent]+1
            self.maxDepth = max(self.maxDepth, nodeMap[root])
            dfs(root.left, root)
            dfs(root.right, root)
        
        dfs(root, None)
        
        def search(node):
            if not node or nodeMap.get(node, None)==self.maxDepth:
                return node
            left = search(node.left)
            right = search(node.right)
            
            if left and right:
                return node
            else:
                return left or right
        
        return search(root)