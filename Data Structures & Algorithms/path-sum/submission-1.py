# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and abs(target_sum - root.val) == 0:
            return True

        left_subtree = self.hasPathSum(root.left, target_sum - root.val)
        right_subtree = self.hasPathSum(root.right, target_sum - root.val)

        return left_subtree or right_subtree

        