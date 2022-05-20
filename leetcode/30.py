class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        WORD_LENGTH = len(words[0])
        SUBSTR_LENGTH = len(words) * WORD_LENGTH
        word_set = set(words)
        counts = {}
        for w in words:
            if w not in counts:
                counts[w] = 0
            counts[w] += 1

        res = []
        for i in range(len(s) - SUBSTR_LENGTH + 1):
            current_count = counts.copy()
            for j in range(len(words)):
                word = s[i + j * WORD_LENGTH: i + (j + 1) * WORD_LENGTH]
                if word not in word_set:
                    break
                current_count[word] -= 1
            if min(current_count.values()) == 0 and max(current_count.values()) == 0:
                res.append(i)

        return res