class TrieNode:
    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.is_word = False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = self.build_trie(words)
        results = []
        for word in words:
            found, amount = self.find_word(word, trie)
            if found and amount > 1:
                results.append(word)

        return results

    def build_trie(self, words) -> TrieNode:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode(c)
                node = node.children[c]
            node.is_word = True
        return root

    def find_word(self, word, root) -> (bool, int):
        node = root
        for i, c in enumerate(word):
            if c not in node.children:
                return False, 0
            node = node.children[c]
            if node.is_word and len(word[i + 1:]) > 0:
                found, amount = self.find_word(word[i + 1:], root)
                if found:
                    return True, amount + 1
        return node.is_word, 1