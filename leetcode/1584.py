import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        queue = [(0, 0)]
        res = 0
        while len(visited) < len(points):
            dist, to = heapq.heappop(queue)
            if to in visited:
                continue

            res += dist
            visited.add(to)
            for i in range(len(points)):
                if i != to and i not in visited:
                    heapq.heappush(queue, (abs(points[to][0] - points[i][0]) + abs(points[to][1] - points[i][1]), i))

        return res