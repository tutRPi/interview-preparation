# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate_subtree(list(range(1, n + 1)))

    def generate_subtree(self, nums: List[int]) -> List[Optional[TreeNode]]:
        if not nums:
            return [None]

        trees = []

        # generate all possible subtrees
        for i, n in enumerate(nums):
            left_nums = nums[0:i]
            right_nums = nums[i + 1:]

            left_trees = self.generate_subtree(left_nums)
            right_trees = self.generate_subtree(right_nums)

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(n)
                    root.left = left
                    root.right = right
                    trees.append(root)

        return trees
