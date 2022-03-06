# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return root

        if root.val == key:
            # no left child:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # has both childs
                # search for most right node in the left subtree,
                # swap value and delete the bottom node
                swap_node = self.find_most_right_value(root.left)
                old_root_value = root.val
                root.val = swap_node.val
                swap_node.val = old_root_value
                root.left = self.deleteNode(root.left, old_root_value)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        return root

    def find_most_right_value(self, root):
        if root.right is None:
            return root
        return self.find_most_right_value(root.right)