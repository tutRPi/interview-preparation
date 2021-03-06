# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is not None:
            return False

        if self.is_identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_identical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root is None and subRoot is None):
            return True

        # print(root.val if root else None, subRoot.val if subRoot else None)
        if (root is None and subRoot is not None) or (root is not None and subRoot is None) or root.val != subRoot.val:
            return False
        return self.is_identical(root.left, subRoot.left) and self.is_identical(root.right, subRoot.right)