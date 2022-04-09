"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None
        root = Node(node.val)
        stack = [(node, target) for target in node.neighbors]

        visited = set([node])
        mapping = {node: root}

        while stack:
            orig_node, orig_target = stack.pop()
            if orig_target not in mapping:
                mapping[orig_target] = Node(orig_target.val)

            if mapping[orig_target] not in mapping[orig_node].neighbors:
                mapping[orig_node].neighbors.append(mapping[orig_target])

            if orig_target not in visited:
                visited.add(orig_target)
                for t in orig_target.neighbors:
                    stack.append((orig_target, t))

        return root