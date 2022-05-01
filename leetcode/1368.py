class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dists = [[float('inf') for j in range(n)] for i in range(m)]
        dists[m - 1][n - 1] = 0
        queue = [(m - 1, n - 1, grid[m - 1], [n - 1])]
        visited = set()

        while queue:
            point = queue.pop(0)
            if (point[0], point[1]) in visited:
                continue
            visited.add((point[0], point[1]))

            # get dist of direct neighbor
            neighbors = [
                dists[point[0]][point[1] + 1] if point[1] + 1 < n else float('inf'),
                dists[point[0]][point[1] - 1] if point[1] - 1 >= 0 else float('inf'),
                dists[point[0] + 1][point[1]] if point[0] + 1 < m else float('inf'),
                dists[point[0] - 1][point[1]] if point[0] - 1 >= 0 else float('inf'),
            ]
            sign = grid[point[0]][point[1]]
            dists[point[0]][point[1]] = min(dists[point[0]][point[1]], neighbors[sign - 1], 1 + min(neighbors))

            # check neighbors, add those who are pointing to the point at the front of the queue
            for o_i, o_j in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= point[0] + o_i < m and 0 <= point[1] + o_j < n:
                    sign = grid[point[0] + o_i][point[1] + o_j]
                    if (sign == 1 and o_j == -1) \
                            or (sign == 2 and o_j == 1) \
                            or (sign == 3 and o_i == -1) \
                            or (sign == 4 and o_i == 1):
                        queue.insert(0, (point[0] + o_i, point[1] + o_j, sign))
                    else:
                        queue.append((point[0] + o_i, point[1] + o_j, sign))

        return dists[0][0]