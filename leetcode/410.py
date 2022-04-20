class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        total = sum(nums)
        max_val = max(nums)

        min_max_sum = total
        lo, hi = max_val, total
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.split_into_arrays(nums, mid) <= m:
                hi = mid - 1
                min_max_sum = mid
            else:
                lo = mid + 1

        return min_max_sum

    def split_into_arrays(self, nums: List[int], maxSum: int) -> int:
        splits = 1
        agg = 0
        for n in nums:
            if agg + n <= maxSum:
                agg += n
            else:
                splits += 1
                agg = n
        return splits


class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:

        def dfs(pos, m):
            if m == 1:
                return sum(nums[pos:])

            current = 0
            res = float('inf')
            for i in range(pos, len(nums) - m + 1):
                current += nums[i]
                next_min_max = dfs(i + 1, m - 1)
                curr_max = max(current, next_min_max)
                if curr_max > res:
                    break
                res = min(res, curr_max)
            return res

        return dfs(0, m)