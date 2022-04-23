class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        lo, hi = 0, nums[-1]
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.count_dists(nums, mid) >= k:
                hi = mid - 1
                curr_min = mid
            else:
                lo = mid + 1
        return curr_min

    def count_dists(self, nums, max_dist) -> int:
        counts = 0
        i, j = 0, 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= max_dist:
                j += 1
            counts += j - i - 1

        return counts