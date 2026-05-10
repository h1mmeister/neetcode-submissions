# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes_helper(node, max_value):
            if not node:
                return 0

            good_node = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)

            left = good_nodes_helper(node.left, max_value)
            right = good_nodes_helper(node.right, max_value)

            return good_node + left + right
        return good_nodes_helper(root, float("-inf"))
        