# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path
        from the root node down to the nearest leaf node.
        '''
        if not root:
            return 0
        if None in [root.left, root.right]:
        # if one of the branches is None, go down the other to reach the leaf
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
        # if it has both branches, find the shortest path to leaf
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def bstFromPreorder(self, preorder) -> TreeNode:
        root = TreeNode(preorder[0])
        # use stack to store root of each subtree
        stack = [root]
        # Note preorder root -> L -> R
        for val in preorder[1:]:
            # left child
            if val < stack[-1].val:
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left)
            # right child of some parent
            else:
                while stack and stack[-1].val < val:
                    # find the parent
                    last = stack.pop()
                last.right = TreeNode(val)
                stack.append(last.right)
        return root


preorder = [8,5,1,7,10,12]
preorder = [8,5,10,12]
sol = Solution()
root = sol.bstFromPreorder(preorder)
print(sol.minDepth(root))
