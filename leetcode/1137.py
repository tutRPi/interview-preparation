class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1

        nums = [0] * (n + 1)
        nums[1] = nums[2] = 1

        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]

        return nums[n]