class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.n = 1337
        self.set = [None] * self.n

    def myhash(self, val: int) -> int:
        return val % self.n

    def add(self, key: int) -> None:
        h = self.myhash(key)
        if self.set[h] is None:
            self.set[h] = Node(key)
        elif not self.contains(key):
            node = self.set[h]
            while node.next is not None:
                node = node.next
            node.next = Node(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            h = self.myhash(key)
            node = self.set[h]
            if node.val == key:
                self.set[h] = node.next
            else:
                while node.next.val != key:
                    node = node.next
                node.next = node.next.next

    def contains(self, key: int) -> bool:
        h = self.myhash(key)
        node = self.set[h]
        if node is None:
            return False
        while node is not None:
            if node.val == key:
                return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)