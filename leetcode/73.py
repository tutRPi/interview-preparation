class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] *= 2

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.fill_row(matrix, i)
                    self.fill_col(matrix, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] //= 2

    def fill_row(self, matrix, r):
        for i in range(len(matrix[r])):
            if matrix[r][i] != 0:
                matrix[r][i] = 1

    def fill_col(self, matrix, c):
        for i in range(len(matrix)):
            if matrix[i][c] != 0:
                matrix[i][c] = 1