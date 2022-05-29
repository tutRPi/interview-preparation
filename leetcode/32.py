class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(1, len(s)):
            c = s[i]
            if c == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + 2
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] += dp[i - dp[i - 1] - 2]

        return max(dp, default=0)