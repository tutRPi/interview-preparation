import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for p in points:
            dist = Solution.euclidean(p, [0, 0])
            heapq.heappush(queue, (-dist, p))
            if len(queue) > k:
                heapq.heappop(queue)

        return [p[1] for p in queue]

    @staticmethod
    def euclidean(p1, p2) -> float:
        return ((p1[0] + p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5