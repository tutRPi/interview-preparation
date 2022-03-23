# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self._traverse(root, [], targetSum)

    def _traverse(self, root, previous_sums, target_sum) -> int:
        if root is None:
            return 0

        results = 0
        previous_sums = previous_sums.copy()
        previous_sums.append(0)
        for i in range(len(previous_sums)):
            previous_sums[i] += root.val
            if previous_sums[i] == target_sum:
                results += 1

        results += self._traverse(root.left, previous_sums, target_sum)
        results += self._traverse(root.right, previous_sums, target_sum)

        return results
