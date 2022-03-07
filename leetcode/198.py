class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        return self.max_amount(nums, 0, memo)

    def max_amount(self, nums, idx, memo) -> int:
        if not nums[idx:]:
            return 0

        if memo[idx] >= 0:
            return memo[idx]

        if len(nums[idx:]) == 1:
            memo[idx] = nums[idx]
            return memo[idx]

        amount1 = nums[idx] + self.max_amount(nums, idx + 2, memo)
        amount2 = self.max_amount(nums, idx + 1, memo)
        memo[idx] = max(amount1, amount2)
        return memo[idx]