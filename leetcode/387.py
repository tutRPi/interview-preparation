class Solution:
    def firstUniqChar(self, s: str) -> int:
        existences = {}
        for c in s:
            if c not in existences:
                existences[c] = 1
            else:
                existences[c] += 1

        for i, c in enumerate(s):
            if existences[c] == 1:
                return i
        return -1