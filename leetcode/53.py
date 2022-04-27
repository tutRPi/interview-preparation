class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] > nums[i]:
                nums[i] += nums[i - 1]
            max_num = max(max_num, nums[i])

        return max_num