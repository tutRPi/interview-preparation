# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [root]
        while queue:
            node = queue.pop(0)

            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)

            if not queue:
                return node.val