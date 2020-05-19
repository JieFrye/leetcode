# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # take care of base case:
        if not root:
            return '#'
        # Preorder traversal root -> L -> R
        Ls = self.serialize(root.left)
        Rs = self.serialize(root.right)
        return root.val, Ls, Rs
        # root, (Lroot, L, R), (Rroot, L, R)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # take care of base case:
        if data[0] == '#':
            return None
        root = TreeNode(data[0])
        # three layers root -> L -> R
        root.left = self.deserialize(data[1])
        root.right = self.deserialize(data[2])
        return root

codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(codec.serialize(root))  

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
