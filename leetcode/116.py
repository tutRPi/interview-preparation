import math

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        indices = {}
        queue = [(0, root)]
        while queue:
            i, node = queue.pop(0)
            indices[i] = node

            if node.left is not None:
                queue.append((2 * i + 1, node.left))
                queue.append((2 * i + 2, node.right))

        queue = [(0, root)]
        while queue:
            i, node = queue.pop(0)
            if math.log(i + 2, 2) % 1 != 0.0:
                node.next = indices[i + 1]

            if node.left is not None:
                queue.append((2 * i + 1, node.left))
                queue.append((2 * i + 2, node.right))

        return root
