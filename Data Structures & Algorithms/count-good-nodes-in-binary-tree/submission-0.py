# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        if not root:
            return good_nodes

        queue = collections.deque()
        queue.append([root, float('-inf')])

        while queue:
            node, max_value = queue.popleft()

            if node.val >= max_value:
                max_value = max(max_value, node.val)
                good_nodes += 1

            if node.left:
                queue.append([node.left, max_value])
            if node.right:
                queue.append([node.right, max_value])

        return good_nodes


        


        