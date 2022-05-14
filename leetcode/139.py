class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def contains(i) -> bool:
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words and contains(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        words = set(wordDict)
        return contains(0)


