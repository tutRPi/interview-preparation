# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        orig_nodes = []
        curr_node = head
        while curr_node is not None:
            orig_nodes.append(curr_node)
            curr_node = curr_node.next

        head = self.copy_node(head, 0, {}, orig_nodes)
        return head

    def copy_node(self, node: Node, current_index: int, nodes: Dict[int, Node], orig_nodes: List[Node]) -> Node:
        if node is None:
            return None
        if current_index in nodes:
            return nodes[current_index]

        node_copy = Node(node.val)
        nodes[current_index] = node_copy

        node_copy.next = self.copy_node(node.next, current_index + 1, nodes, orig_nodes)
        if node.random is not None:
            random_orig_index = orig_nodes.index(node.random)
            node_copy.random = self.copy_node(orig_nodes[random_orig_index], random_orig_index, nodes, orig_nodes)

        return node_copy