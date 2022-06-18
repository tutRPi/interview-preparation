# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counts = 0
        self.path(root, root.val)
        return self.counts

    def path(self, node, X):
        if node is None:
            return

        if X <= node.val:
            self.counts += 1
            X = node.val

        self.path(node.left, X)
        self.path(node.right, X)