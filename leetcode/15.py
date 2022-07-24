class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()

        res = []

        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, N - 1
            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if t == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < N - 1 and nums[left - 1] == nums[left]:
                        left += 1

                elif t < 0:
                    left += 1
                else:
                    right -= 1

        return res