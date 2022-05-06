# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [(0, root)]
        result = []
        while queue:
            level, node = queue.pop(0)
            if len(result) == level:
                result.append(node.val)

            if node.right is not None:
                queue.append((level + 1, node.right))
            if node.left is not None:
                queue.append((level + 1, node.left))

        return result