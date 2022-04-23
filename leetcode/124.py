class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        self.find_max_subpath(root)
        return self.max_sum

    def find_max_subpath(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            self.max_sum = max(self.max_sum, root.val)
            return root.val

        if root.left is not None and root.right is not None:
            left_sum = self.find_max_subpath(root.left)
            right_sum = self.find_max_subpath(root.right)
            max_sum = root.val + max(0, left_sum, right_sum, left_sum + right_sum)
            self.max_sum = max(self.max_sum, max_sum)
            return root.val + max(0, left_sum, right_sum)

        elif root.left is not None:
            max_child_sum = self.find_max_subpath(root.left)
            max_sum = max(root.val, root.val + max_child_sum)
        else:
            max_child_sum = self.find_max_subpath(root.right)
            max_sum = max(root.val, root.val + max_child_sum)

        self.max_sum = max(self.max_sum, max_sum)
        return max_sum