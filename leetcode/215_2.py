import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        queue = []
        for n in nums:
            heapq.heappush(queue, n)
            if len(queue) > k:
                heapq.heappop(queue)
        return heapq.heappop(queue)


if __name__ == "__main__":
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
