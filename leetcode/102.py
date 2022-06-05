# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        level = 0
        queue = [(root, 1)]
        while queue:
            node, lv = queue.pop(0)

            if lv != level:
                level = lv
                result.append([])

            result[-1].append(node.val)

            if node.left is not None:
                queue.append((node.left, lv + 1))
            if node.right is not None:
                queue.append((node.right, lv + 1))

        return result