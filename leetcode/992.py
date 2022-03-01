class Solution:
    def subarraysWithKDistinct(self, nums: list, k: int) -> int:

        count = 0
        for length in range(k, len(nums) + 1):
            for i in range(len(nums) + 1 - length):
                if len(set(nums[i:i + length])) == k:
                    count += 1
        return count


if __name__ == "__main__":
    assert Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7
    assert Solution().subarraysWithKDistinct([1,2,1,3,4], 3) == 3
    assert Solution().subarraysWithKDistinct([1,2,1,3,4], 3) == 3
