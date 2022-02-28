class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num_array = [int(n) for n in nums]
        num_array = sorted(num_array)
        return str(num_array[-k])