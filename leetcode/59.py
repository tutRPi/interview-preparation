class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for j in range(n)]

        idx = 1
        pos_x, pos_y = 0, 0
        m = n
        while m > 1:
            for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                for _ in range(m - 1):
                    matrix[pos_y][pos_x] = idx
                    pos_x += dx
                    pos_y += dy
                    idx += 1
                print()
            pos_x += 1
            pos_y += 1

            m -= 2

        if m == 1:
            matrix[n // 2][n // 2] = idx

        return matrix