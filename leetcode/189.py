class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        buffer = nums[-k:]

        for i in reversed(range(k, len(nums))):
            nums[i] = nums[i - k]

        for i in range(k):
            nums[i] = buffer[i]