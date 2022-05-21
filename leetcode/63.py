class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        paths = [[0] * (COLS + 1) for i in range(ROWS + 1)]
        paths[ROWS - 1][COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    continue

                if obstacleGrid[r][c] == 0:
                    paths[r][c] = paths[r + 1][c] + paths[r][c + 1]

        return paths[0][0]