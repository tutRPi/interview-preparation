class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return max(nums)

        start0 = nums.copy()
        start1 = nums.copy()
        start0[-1] = -start0[0]
        start1[0] = 0
        start0[2] += start0[0]

        for i in range(3, len(nums)):
            start0[i] += max(start0[i - 2], start0[i - 3])
            start1[i] += max(start1[i - 2], start1[i - 3])

        return max(max(start0), max(start1))