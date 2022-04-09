class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] <= nums[m] < nums[r]:
                return nums[l]
            elif nums[m] < nums[r] < nums[l]:
                r = m
            else:
                l = m + 1

        return nums[l]