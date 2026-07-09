# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.inorder_traversal(root, inorder)
        return inorder[k - 1]

    def inorder_traversal(self, node, array):
        if node is None: # if not Node:
            return 

        self.inorder_traversal(node.left, array)
        array.append(node.val)
        self.inorder_traversal(node.right, array)

        return
        
        