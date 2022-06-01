class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        memo = {}

        def dfs(i, target_sum) -> bool:
            if target_sum == 0:
                return True
            if i == len(nums) or target_sum < 0:
                return False
            if (i, target_sum) in memo:
                return memo[(i, target_sum)]

            result = dfs(i + 1, target_sum - nums[i]) or dfs(i + 1, target_sum)
            memo[(i, target_sum)] = result
            return result

        return dfs(0, s / 2)