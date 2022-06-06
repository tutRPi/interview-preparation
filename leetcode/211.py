class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._dfs(word, self.root)

    def _dfs(self, word: str, node: TrieNode) -> bool:

        for i in range(len(word)):
            if word[i] == ".":
                for c in node.children:
                    if self._dfs(word[i + 1:], node.children[c]):
                        return True
                return False
            elif word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False
        return node.is_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)