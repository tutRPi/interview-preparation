import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = -1 * heapq.heappop(heap)
            s2 = -1 * heapq.heappop(heap)
            res = s1 - s2
            heapq.heappush(heap, -1 * res)
        return heap[0] * -1