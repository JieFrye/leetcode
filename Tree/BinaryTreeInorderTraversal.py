# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #def inorderTraversal(self, root: TreeNode) -> List[int]:
    #    vals = []
    #    self.dfs(root, vals)
    #    return vals
    # Left -> Root -> Right
    #def dfs(self, root, vals):
    #    if root:
    #        self.dfs(root.left, vals)
    #        vals.append(root.val)
    #        self.dfs(root.right, vals)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # interative Left -> Root -> Right:
        vals, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left # get all layers of left subtree
            if not stack: # at the end of the operation
                return vals
            node = stack.pop()
            vals.append(node.val)
            # move to the right subtree and traverse inorder
            root = node.right
