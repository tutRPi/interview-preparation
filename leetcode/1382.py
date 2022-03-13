# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        node_queue = [root]
        sorted_values = []

        while node_queue:
            node = node_queue.pop(0)

            sorted_values.append(node.val)

            if node.left is not None:
                node_queue.append(node.left)

            if node.right is not None:
                node_queue.append(node.right)
                print(node.right.val)

        sorted_values = sorted(sorted_values)

        new_root = self.create_binary_search_tree(sorted_values)
        return new_root

    def create_binary_search_tree(self, sorted_values) -> TreeNode:

        if not sorted_values:
            return None

        value_index = int(len(sorted_values) / 2)
        root = TreeNode(sorted_values[value_index])
        root.left = self.create_binary_search_tree(sorted_values[0:value_index])
        root.right = self.create_binary_search_tree(sorted_values[value_index + 1:])

        return root
