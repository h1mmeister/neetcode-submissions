# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = []
        queue.append(root)

        while queue:
            level = []
            for _ in range(0, len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result
                


        