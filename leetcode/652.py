# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicates = []
        paths = {}
        self.dfs(root, paths, duplicates)
        return duplicates

    def dfs(self, node, paths, duplicates) -> str:
        if node is None:
            return "."
        left = self.dfs(node.left, paths, duplicates)
        right = self.dfs(node.right, paths, duplicates)
        s = str(node.val) + "|" + left + "," + right
        if s in paths:
            if paths[s][1] == 1:
                duplicates.append(node)
            paths[s] = (paths[s][0], paths[s][1] + 1)
        else:
            paths[s] = (node, 1)
        return s