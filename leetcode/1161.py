# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        min_level = -1

        children = [root]
        level = 0
        while children:
            level += 1
            level_sum = 0
            next_children = []
            for child in children:
                level_sum += child.val
                if child.left is not None: next_children.append(child.left)
                if child.right is not None: next_children.append(child.right)

            children = next_children
            if level_sum > max_sum:
                max_sum = level_sum
                min_level = level
        return min_level
