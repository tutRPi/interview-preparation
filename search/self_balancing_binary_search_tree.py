# Balanced Binary Tree Definition
# A binary tree in which the left and right subtree of each node differ in height by no more than 1
# Example [3, 9, 20, null, null, 15, 7]
#     15
#    / \
#   7   20
#       / \
#      18  27

from typing import Optional
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.binary_tree_printer import print_binary_tree

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left: Node = left
        self.right: Node = right
        self.balance_factor: int = 0
        self.height: int = 0


class SelfBalancingBinarySearchTree:
    def __init__(self, data=None):
        if data is not None:
            self.__root: Optional[Node] = Node(data)
            self.__size = 1
        else:
            self.__root: Optional[Node] = None
            self.__size = 0

    def root_node(self):
        return self.__root

    def is_empty(self):
        return self.size() == 0

    def size(self) -> int:
        return self.__size

    def contains(self, data) -> bool:
        found = False
        node = self.__root
        while not found and node is not None:
            if node.data == data:
                found = True
            elif node.data < data:
                node = node.right
            else:
                node = node.left
        return found

    def add(self, data) -> bool:
        if not self.contains(data):
            self.__root = self.__add(self.__root, data)
            self.__size += 1
        else:
            return False
        return True

    def __add(self, node: Node, data) -> Node:
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.__add(node.left, data)
        else:
            node.right = self.__add(node.right, data)

        self.__update(node)
        return self.__self_balance(node)

    def remove(self, data) -> bool:
        if self.contains(data):
            self.__root = self.__remove(self.__root, data)
            self.__size -= 1
            return True
        return False

    def __remove(self, node: Node, data) -> Node:
        if node.data == data:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                if node.left.height > node.right.height:
                    # replace with most left value of the right subtree
                    tmp = self.__find_most_left_node(node.right)
                    node.data = tmp.data
                    node.right = self.__remove(node.right, tmp.data)
                else:
                    tmp = self.__find_most_right_node(node.left)
                    node.data = tmp.data
                    node.left = self.__remove(node.left, tmp.data)

        elif data < node.data:
            # search in left subtree
            node.left = self.__remove(node.left, data)
        elif data > node.data:
            # search in right subtree
            node.right = self.__remove(node.right, data)

        self.__update(node)
        return self.__self_balance(node)

    def __find_most_left_node(self, node: Node) -> Optional[Node]:
        if node.left is None:
            return node
        return self.__find_most_left_node(node.left)

    def __find_most_right_node(self, node: Node) -> Optional[Node]:
        if node.right is None:
            return node
        return self.__find_most_right_node(node.left)

    @staticmethod
    def __update(node: Node):
        lh = node.left.height if node.left is not None else -1
        rh = node.right.height if node.right is not None else -1
        node.height = 1 + max(lh, rh)
        node.balance_factor = rh - lh

    # returns new parent after rebalancing
    def __self_balance(self, node: Node) -> Node:
        if node.balance_factor == -2:
            if node.left.balance_factor <= 0:
                return self.__left_left_case(node)
            else:
                return self.__left_right_case(node)
        elif node.balance_factor == 2:
            if node.right.balance_factor <= 0:
                return self.__right_left_case(node)
            else:
                return self.__right_right_case(node)
        return node

    def __left_left_case(self, node: Node):
        return self.__right_rotate(node)

    def __left_right_case(self, node: Node):
        node.left = self.__left_rotate(node.left)
        return self.__right_rotate(node)

    def __right_right_case(self, node: Node):
        return self.__left_rotate(node)

    def __right_left_case(self, node: Node):
        node.right = self.__right_rotate(node.right)
        return self.__right_right_case(node)

    def __right_rotate(self, node: Node):
        p = node.left
        node.left = p.right
        p.right = node
        self.__update(node)
        self.__update(p)
        return p

    def __left_rotate(self, node: Node):
        p = node.right
        node.right = p.left
        p.left = node
        self.__update(node)
        self.__update(p)
        return p

    @staticmethod
    def __is_balanced(self, node: Optional[Node]) -> (bool, int, int):
        if node is None:
            return True, 0, 0
        left = self.__is_balanced(node.left) - 1
        right = self.__is_balanced(node.right) - 1
        return left[0] and right[0] and abs(left[1] - right[1]) <= 1, 1 + max(left[1], right[1]), left[1] - right[1]


if __name__ == '__main__':
    tree = SelfBalancingBinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    tree.add(11)
    tree.add(12)
    print_binary_tree(tree.root_node())

    assert tree.remove(9) is True
    print_binary_tree(tree.root_node())
