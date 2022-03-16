# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.index = 0
        # iterative inorder traversal
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.nodes.append(root.val)
            root = root.right        

    def next(self) -> int:
        res = self.nodes[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        if self.index >= len(self.nodes):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()