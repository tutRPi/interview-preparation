class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = TrieNode()
        for word in dictionary:
            node = root
            for l in word:
                if l not in node.children:
                    node.children[l] = TrieNode(l)
                node = node.children[l]
            node.is_word = True

        words = sentence.split(" ")
        result = []
        for word in words:
            prefix = self.find_prefix(word, root)
            result.append(prefix if prefix else word)

        return " ".join(result)

    def find_prefix(self, word, root) -> Optional[str]:
        result = ""
        for l in word:
            if root.is_word:
                if result:
                    return result
                else:
                    return None
            elif l in root.children:
                result += l
                root = root.children[l]
            else:
                break
        return None
