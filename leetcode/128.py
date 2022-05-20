class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = {n: 1 for n in nums}

        visited = set()

        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            if n + 1 in longest:
                dfs(n + 1)
                longest[n] = 1 + longest[n + 1]

        for n in nums:
            dfs(n)

        return max(longest.values(), default=0)