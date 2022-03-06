class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length = len(nums)
        max_subsequences = [1] * length
        for i in reversed(range(length - 1)):
            stack = [0]
            for j in range(i + 1, length):
                if nums[i] < nums[j]:
                    stack.append(max_subsequences[j])
            max_subsequences[i] += max(stack)

        return max(max_subsequences)