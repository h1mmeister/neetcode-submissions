# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate_bst_helper(root, float("-inf"), float("inf"))

    def validate_bst_helper(self, node, min_value, max_value):
        if not node:
            return True

        if node.val <= min_value or node.val >= max_value:
            return False
            
        left_subtree = self.validate_bst_helper(node.left, min_value, node.val)
        right_subtree = self.validate_bst_helper(node.right, node.val, max_value)
        return left_subtree and right_subtree

    


        