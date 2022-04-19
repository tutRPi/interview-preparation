class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        max_val = 0
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    if i >= 1 and j >= 1:
                        min_neighbor = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1])
                        matrix[i][j] += min_neighbor
        max_length = max(map(max, matrix))
        return max_length ** 2