from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self._traverse(root, [], 0, targetSum)

    def _traverse(self, root, prev_nums: List[int], prev_sum, target_sum) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            if prev_sum + root.val == target_sum:
                return [prev_nums + [root.val]]
            else:
                return []
        else:
            result = []
            for path in self._traverse(root.left, prev_nums + [root.val], prev_sum + root.val, target_sum):
                result.append(path)
            for path in self._traverse(root.right, prev_nums + [root.val], prev_sum + root.val, target_sum):
                result.append(path)
            return result

