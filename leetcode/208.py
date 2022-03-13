class Node:
    def __init__(self):
        self.keys = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str, node: Node = None) -> None:
        if node is None:
            node = self.root

        if not word:
            node.is_end = True
        else:
            if word[0] not in node.keys:
                node.keys[word[0]] = Node()
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.keys:
                return False
            node = node.keys[letter]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.keys:
                return False
            node = node.keys[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)