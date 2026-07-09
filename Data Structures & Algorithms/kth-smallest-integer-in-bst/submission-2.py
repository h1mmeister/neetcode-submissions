# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self, nodes_visited, result):
        self.nodes_visited = nodes_visited
        self.result = result

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        treeinfo = TreeInfo(0, -1)
        self.inorder_traversal(root, k, treeinfo)
        return treeinfo.result

    def inorder_traversal(self, node, k, treeinfo):
        if not node:
            return TreeInfo(0, -1)

        self.inorder_traversal(node.left, k, treeinfo)
        if treeinfo.nodes_visited < k:
            treeinfo.nodes_visited += 1
            treeinfo.result = node.val
            self.inorder_traversal(node.right, k, treeinfo)
        