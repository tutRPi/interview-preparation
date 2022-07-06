class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        if len(s) == 1:
            return [[s]]

        res = []
        for i in range(1, len(s) + 1):
            if self.is_palindrom(s[:i]):
                others = self.partition(s[i:])
                if others:
                    for other in others:
                        res.append([s[:i]] + other)

        return res

    def is_palindrom(self, s):
        if len(s) <= 1:
            return True
        if len(s) == 2:
            return s[0] == s[1]

        return s[0] == s[-1] and self.is_palindrom(s[1:-1])