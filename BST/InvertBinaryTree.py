# Invert a binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        idea: recursion
        '''
        if not root:
            return None
        # invert the left and right subtrees from bottom up
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        root.left = r
        root.right = l
        return root
