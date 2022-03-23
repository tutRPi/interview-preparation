class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        overall_sum = sum(nums)
        if overall_sum % 2 == 1:
            return False

        # 0/1 knapsack problem for overall_sum/2
        all_variations = set()
        for n in nums:
            prev_sums = list(all_variations)
            for prev_sum in prev_sums:
                all_variations.add(n + prev_sum)
            all_variations.add(n)

        return overall_sum / 2 in all_variations
