class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        nums.insert(0, float("-inf"))
        nums.append(float("inf"))
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left - 1