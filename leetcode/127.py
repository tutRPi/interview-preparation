class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        transformations = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                comb = word[:i] + "*" + word[i + 1:]
                transformations[comb].append(word)

        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            word, count = queue.pop(0)
            if word == endWord:
                return count

            if word in visited:
                continue
            visited.add(word)

            for i in range(len(word)):
                comb = word[:i] + "*" + word[i + 1:]
                for trans in transformations[comb]:
                    if trans not in visited:
                        queue.append((trans, count + 1))

        return 0