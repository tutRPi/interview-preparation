class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(i1, i2, i3) -> bool:
            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2)

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            res = False
            if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2] == s3[i3]:
                res = dfs(i1 + 1, i2, i3 + 1) or dfs(i1, i2 + 1, i3 + 1)
            elif i1 < len(s1) and s1[i1] == s3[i3]:
                res = dfs(i1 + 1, i2, i3 + 1)
            elif i2 < len(s2) and s2[i2] == s3[i3]:
                res = dfs(i1, i2 + 1, i3 + 1)

            memo[(i1, i2)] = res
            return memo[(i1, i2)]

        return dfs(0, 0, 0)