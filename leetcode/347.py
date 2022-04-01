class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        frequency = [[] for _ in range(len(nums) + 1)]
        for n, count in counts.items():
            frequency[count].append(n)

        frequency = [item for a in frequency for item in a if len(a) > 0]
        return frequency[-k:]