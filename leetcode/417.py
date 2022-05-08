import heapq


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        closest = [[(None, None)] * n for _ in range(m)]

        queue = [(heights[i][j], (i, j)) for j in range(n) for i in range(m)]
        heapq.heapify(queue)

        res = []

        while queue:
            elem = heapq.heappop(queue)

            stack = [elem]
            visited = set()
            pacific, atlantic = False, False
            while stack and not (pacific and atlantic):
                val, pos = stack.pop()
                visited.add(pos)

                if pos[0] == 0 or pos[1] == 0:
                    pacific = True
                if pos[0] == m - 1 or pos[1] == n - 1:
                    atlantic = True

                for oi, oj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i = max(0, min(pos[0] + oi, m - 1))
                    j = max(0, min(pos[1] + oj, n - 1))
                    if (i, j) not in visited and heights[i][j] <= val:
                        stack.append((heights[i][j], (i, j)))

            if pacific and atlantic:
                res.append(elem[1])

        return res