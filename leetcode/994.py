class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = {(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 0}
        queue = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 2]
        minutes = -2

        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited:
                    continue

                visited.add((i, j))

                grid[i][j] = 2

                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))

            minutes += 1

        return max(0, minutes) if len(visited) == ROWS * COLS else -1