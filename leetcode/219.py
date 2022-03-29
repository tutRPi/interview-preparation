class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_pos = {}
        for i, n in enumerate(nums):
            if n in last_pos:
                if i - last_pos[n] <= k:
                    return True
            last_pos[n] = i
        return False