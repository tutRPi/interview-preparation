class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1

            if s[i] == "0":
                memo[i] = 0
                return 0
            elif i == len(s) - 1:
                return 1
            else:
                memo[i] = dfs(i + 1)
                if i + 2 <= len(s) and int(s[i:i + 2]) <= 26:
                    memo[i] += dfs(i + 2)
                return memo[i]

        memo = {}
        return dfs(0)


if __name__ == "__main__":
    assert Solution().numDecodings("") == 0
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("110") == 1
    assert Solution().numDecodings("27") == 1
    assert Solution().numDecodings("2101") == 1
    assert Solution().numDecodings("11106") == 2
    assert Solution().numDecodings("123123") == 9
    assert Solution().numDecodings("252353") == 4