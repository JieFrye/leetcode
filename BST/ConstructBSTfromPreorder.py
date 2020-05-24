# Return the root node of a binary search tree
# that matches the given preorder traversal.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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


L = [8,5,1,7,10,12]
sol = Solution()
root = sol.bstFromPreorder(L)

# Given a binary tree, print the level order traversal
def traverse(root):
    if not root:
        return
    ans, q = [], [root]
    while q:
        ans[:0] = [[node.val for node in q]]
        level = []
        for node in q:
            level.extend([node.left, node.right])
        # update q
        q = [e for e in level if e]
    return ans

print(traverse(root))
