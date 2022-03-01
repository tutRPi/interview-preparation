# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.construct_tree(preorder)

    def construct_tree(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # find value that is greater than root node, to split
        index = len(preorder)
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                index = i
                break

        left_child = self.construct_tree(preorder[1:index])
        right_child = self.construct_tree(preorder[index:])
        root = TreeNode(preorder[0], left_child, right_child)
        return root

