# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return ["->".join(path) for path in self.dfs(root)]

    def dfs(self, root) -> List[List[str]]:

        if root.left is None and root.right is None:
            return [[str(root.val)]]

        results = []
        if root.left is not None:
            paths = self.dfs(root.left)
            for child in paths:
                results.append([str(root.val)] + child)
        if root.right is not None:
            paths = self.dfs(root.right)
            for child in paths:
                results.append([str(root.val)] + child)

        return results