# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        return self.has_path_helper(root, target_sum, curr_sum = 0)

    def has_path_helper(self, node, target_sum, curr_sum):
        if not node:
            return False

        curr_sum += node.val
        if not node.left and not node.right and curr_sum == target_sum:
            return True

        left_subtree = self.has_path_helper(node.left, target_sum, curr_sum)
        right_subtree = self.has_path_helper(node.right, target_sum, curr_sum)

        return left_subtree or right_subtree
        