class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[right] < target < nums[left]:
            return -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif (nums[left] < nums[mid] < nums[right] and target < nums[mid]) \
                    or (nums[left] > nums[right] > nums[mid] and (target < nums[mid] or nums[left] <= target)) \
                    or (nums[mid] > nums[left] > nums[right] and nums[left] <= target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return -1