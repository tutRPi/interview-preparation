import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        counts = defaultdict(int)
        for c in tasks:
            counts[c] += 1

        queue = [-val for val in counts.values()]
        heapq.heapify(queue)

        units = 0
        while queue:
            res = []
            for i in range(n + 1):
                if queue:
                    res.append(heapq.heappop(queue) + 1)

            if abs(min(res)) == 0 and len(res) <= n:
                units += len(res)
            else:
                units += n + 1

            for val in res:
                if val != 0:
                    heapq.heappush(queue, val)

        return units