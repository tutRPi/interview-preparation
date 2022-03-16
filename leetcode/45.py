class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [0] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            steps[i] = 1 + min(steps[i + 1: i + 1 + nums[i]], default=float('inf'))
        return steps[0]