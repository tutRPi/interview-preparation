import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.binary_tree_printer import print_binary_tree


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    __node_count: int = 0
    __root: Node = None

    def root_node(self):
        return self.__root

    def is_empty(self) -> bool:
        return self.__node_count == 0

    def size(self):
        return self.__node_count

    def contains(self, x) -> bool:
        found = False
        node = self.__root
        while node is not None and not found:
            if node.data == x:
                found = True
            elif node.data > x:
                node = node.left
            elif node.data < x:
                node = node.right

        return found

    def add(self, data):
        if self.is_empty():
            self.__root = Node(data)
            self.__node_count += 1
        else:
            # do not accept same values
            if not self.contains(data):
                self.__add(self.__root, data)

    def __add(self, node: Node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                self.__node_count += 1
            else:
                self.__add(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
                self.__node_count += 1
            else:
                self.__add(node.right, data)

    def remove(self, x) -> bool:
        if self.contains(x):
            self.__root = self.__remove(self.__root, x)
            self.__node_count -= 1
            return True
        else:
            return False

    def __remove(self, node: Node, x) -> Node:
        if node.data == x:
            if node.left is None:
                right_child = node.right
                node = None  # delete node
                return right_child
            elif node.right is None:
                left_child = node.left
                node = None  # delete node
                return left_child
            else:
                # both not None, find greatest value (most right) in left subtree,
                # or alternatively lowest in right subtree (most left)
                tmp = self.__dig_right(node.left)
                # copy data from most right (greatest) node of left subtree
                node.data = tmp.data
                # remove the node with that value in the left subtree (will not affect current node)
                node.left = self.__remove(node.left, tmp.data)
        elif node.data < x:
            node.left = self.__remove(node.right, x)
        elif node.data > x:
            node.right = self.__remove(node.left, x)

        return node

    def __dig_right(self, node: Node):
        n = node
        while n.right is not None:
            n = self.__dig_right(node.right)
        return n


if __name__ == '__main__':
    #       7
    #    /      \
    #   4       12
    #  /  \    /   \
    # 2    5  8    13

    tree = BinarySearchTree()
    tree.add(7)
    tree.add(12)
    tree.add(8)
    tree.add(4)
    tree.add(5)
    tree.add(2)
    tree.add(13)
    tree.add(5)  # duplicate
    tree.add(13)  # duplicate

    assert tree.contains(5) is True
    assert tree.contains(9) is False
    assert tree.size() == 7

    print_binary_tree(tree.root_node())

    assert tree.remove(1) is False
    assert tree.remove(7) is True
    assert tree.remove(5) is True
    assert tree.remove(4) is True
    assert tree.size() == 4

    print_binary_tree(tree.root_node())
