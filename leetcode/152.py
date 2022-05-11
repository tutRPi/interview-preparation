class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_min = [None] * len(nums)
        curr_max = [None] * len(nums)
        curr_min[0] = curr_max[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0 or curr_min[i - 1] == 0:
                curr_min[i] = curr_max[i] = nums[i]
            else:
                if nums[i] < 0:
                    if curr_min[i - 1] < 0:
                        curr_min[i] = min(nums[i], curr_max[i - 1] * nums[i])
                        curr_max[i] = curr_min[i - 1] * nums[i]
                    else:
                        curr_min[i] = curr_min[i - 1] * nums[i]
                        curr_max[i] = nums[i]
                else:
                    curr_min[i] = curr_min[i - 1] * nums[i]
                    if curr_max[i - 1] > 0:
                        curr_max[i] = curr_max[i - 1] * nums[i]
                    else:
                        curr_max[i] = nums[i]
        return max(curr_max)