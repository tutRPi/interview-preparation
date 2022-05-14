class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []

        row_boundaries = [0, ROWS - 1]
        col_boundaries = [0, COLS - 1]
        r, c = 0, 0
        r_direction, c_direction = 0, 1

        while row_boundaries[0] <= row_boundaries[1] and col_boundaries[0] <= col_boundaries[1]:
            print(r, c, row_boundaries, col_boundaries)
            res.append(matrix[r][c])
            if c_direction == 1 and c == col_boundaries[1]:
                # down
                r_direction, c_direction = 1, 0
                row_boundaries[0] += 1
            elif r_direction == 1 and r == row_boundaries[1]:
                # left
                r_direction, c_direction = 0, -1
                col_boundaries[1] -= 1
            elif c_direction == -1 and c == col_boundaries[0]:
                # up
                r_direction, c_direction = -1, 0
                row_boundaries[1] -= 1
            elif r_direction == -1 and r == row_boundaries[0]:
                # right
                r_direction, c_direction = 0, 1
                col_boundaries[0] += 1

            r += r_direction
            c += c_direction

        return res