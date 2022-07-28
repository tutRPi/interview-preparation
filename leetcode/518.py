class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(rest, i) -> int:
            if rest == 0:
                return 1
            if rest < 0 or i >= len(coins):
                return 0

            if (rest, i) in memo:
                return memo[(rest, i)]

            memo[(rest, i)] = dfs(rest, i + 1) + dfs(rest - coins[i], i)
            return memo[(rest, i)]

        return dfs(amount, 0)