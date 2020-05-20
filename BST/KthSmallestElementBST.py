# May 20 Challenge

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        In-Order traversal on a BST visit the values in ascending order
        L -> root -> R
        '''
        inorder, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left # get all layers of left subtree
            if not stack: # at the end of the operation
                return inorder[k-1]
            node = stack.pop()
            inorder.append(node.val)
            # move to the right subtree and traverse inorder
            root = node.right

# Construct the BST from its given level order traversal.
def leveltoBST(array):
    root = None
    for i in range(len(array)):
        if not root:
            root = TreeNode(array[i])
        else:
            BSTinsert(root, array[i])
    return root

def BSTinsert(root, val):
    if val < root.val:
        if root.left:
            BSTinsert(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            BSTinsert(root.right, val)
        else:
            root.right = TreeNode(val)

# print preorder
def traverse(root):
    if not root:
        return
    print("-> ", root.val)
    traverse(root.left)
    traverse(root.right)

# root = [3,1,4,0,2]
root = [7,4,12,3,6,8,1,5,10]
# root = [3,1,4,2]
# root = [5,3,6,2,4,1]
k = 3
r = leveltoBST(root)
# print(r)
# list = traverse(r)
# print(list)
sol = Solution()
print(sol.kthSmallest(r, k))
