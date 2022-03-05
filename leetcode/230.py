# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, 1, k)[2]

    def dfs(self, node, current_position, target_position) -> (
    bool, int, Optional[int]):  # (found, new_position, number)

        if node.left:
            (found, current_position, result) = self.dfs(node.left, current_position, target_position)
            if found:
                return (True, current_position, result)

        if current_position == target_position:
            return (True, current_position, node.val)

        current_position += 1
        if node.right:
            (found, current_position, result) = self.dfs(node.right, current_position, target_position)
            if found:
                return (True, current_position, result)

        return (False, current_position, None)
