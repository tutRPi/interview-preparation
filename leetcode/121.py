class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = [0] * len(prices)
        max_right[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], prices[i + 1])

        profit = 0
        for i in range(len(prices) - 1):
            profit = max(profit, max_right[i] - prices[i])

        return profit