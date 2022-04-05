# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # post-order traversal
        if not root:
            return "#"
        serialTree = str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
        return serialTree
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(l):
            if l[0]=='#':
                l.pop(0)
                return None
            root = TreeNode(int(l[0]))
            # pop the first element
            l.pop(0)
            root.left = dfs(l)
            root.right = dfs(l)
            
            return root
        
        data_list = data.split(",")
        return dfs(data_list)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))