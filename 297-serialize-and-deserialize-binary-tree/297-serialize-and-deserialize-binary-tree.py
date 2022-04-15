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
        if not root:
            return "#"
        
        return str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dlist = data.split(",")
        
        def dfs(dlist):
            if dlist[0]=='#':
                dlist.pop(0)
                return None
            
            root = TreeNode(dlist[0])
            # remove the current element
            dlist.pop(0)
            root.left = dfs(dlist)
            root.right = dfs(dlist)
            return root
        
        return dfs(dlist)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))