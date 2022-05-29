class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        def dfs(start, splits) -> int:
            if splits == 0:
                return max(jobDifficulty[start:])

            if (start, splits) in memo:
                return memo[(start, splits)]

            min_val = float('inf')
            for i in range(start + 1, len(jobDifficulty) - splits + 1):
                curr_max = max(jobDifficulty[start:i])
                min_val = min(min_val, curr_max + dfs(i, splits - 1))

            memo[(start, splits)] = min_val
            return min_val

        memo = {}

        return dfs(0, d - 1)