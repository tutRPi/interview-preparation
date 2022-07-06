class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        land = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 1]

        visited = set()
        res = 0
        for r, c in land:
            if (r, c) in visited:
                continue

            island = 0
            queue = [(r, c)]
            while queue:
                i, j = queue.pop()
                if (i, j) in visited or i < 0 or j < 0 or i >= ROWS or j >= COLS:
                    continue

                visited.add((i, j))

                if grid[i][j] == 0:
                    continue

                island += 1
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))

            res = max(res, island)

        return res