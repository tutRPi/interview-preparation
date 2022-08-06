class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        def dfs(n):
            if n < 0:
                return float('inf')
            if n in memo:
                return memo[n]

            if n in coins:
                memo[n] = 1
                return 1
            else:
                needed = float('inf')
                for c in coins:
                    needed = min(needed, 1 + dfs(n - c))
                memo[n] = needed
                return needed

        memo = {}
        res = dfs(amount)
        return res if res != float('inf') else -1