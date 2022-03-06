class Solution:
    def canJump(self, nums: List[int]) -> bool:

        length = len(nums)
        can_reach_end = [False] * length
        can_reach_end[-1] = True

        for i in reversed(range(length - 1)):
            steps = nums[i]
            if i + steps >= length:
                can_reach_end[i] = True
            elif steps != 0:
                can_reach_end[i] = any(can_reach_end[i + 1:i + 1 + steps])

        print(can_reach_end)
        return can_reach_end[0]