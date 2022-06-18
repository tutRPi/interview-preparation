class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {0: 0, 1: 0, 2: 0}
        for i in nums:
            counts[i] += 1

        for i in range(counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[0] + counts[1]):
            nums[i] = 1
        for i in range(counts[0] + counts[1], len(nums)):
            nums[i] = 2