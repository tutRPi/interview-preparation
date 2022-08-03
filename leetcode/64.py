class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path_length = grid.copy()

        for r in range(ROWS):
            for c in range(COLS):
                if r == c == 0:
                    continue

                top = path_length[r - 1][c] if r > 0 else float('inf')
                left = path_length[r][c - 1] if c > 0 else float('inf')

                path_length[r][c] += min(top, left)

        return path_length[-1][-1]