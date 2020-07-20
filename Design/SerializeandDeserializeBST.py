# Serialize and Deserialize BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
             5
            / \
          2     8
         / \     \
        1   3     9
        """
        vals = []
        def preorderString(node):
            if node:
                vals.append(str(node.val))
                preorderString(node.left)
                preorderString(node.right)
        # build the string '5 2 1 3 8 9'
        preorderString(root)
        return ' '.join(vals)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        Need to keep track of L and R trees
        """
        vals = collections.deque(int(v) for v in data.split())
        def preorderTree(min, max):
            if vals and min < vals[0] < max:
                root_val = vals.popleft()
                root = TreeNode(root_val)
                root.left = preorderTree(min, root_val)
                root.right = preorderTree(root_val, max)
                return root
        return preorderTree(float('-inf'), float('inf'))




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
