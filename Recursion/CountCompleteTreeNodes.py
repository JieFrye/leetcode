# Count Complete Tree Nodes
# Given a complete binary tree, count the number of nodes.
# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        '''
        ideas:
        Use complete BT property to optimize the solution.
        At level l, there are 2**l number of nodes.
        (1) if left subtree and right subtree have the same depth,
            then the left subtree is a full binary tree.
        (2) if left subtree and right subtree have different depth,
            then the right subtree is a full binary tree.
        '''
        if not root:
            return 0
        L = self.getDepth(root.left)
        R = self.getDepth(root.right)
        if L == R:
            return 2**L + self.countNodes(root.right)
        else:
            return 2**R + self.countNodes(root.left)

    # get the depth
    def getDepth(self, root):
        if not root:
            return 0
        else:
            # all nodes in the last level are as far left as possible
            return 1 + self.getDepth(root.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
sol = Solution()
print(sol.countNodes(root))
