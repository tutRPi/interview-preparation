class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(n // 2):
                val = matrix[n - 1 - j][i]
                for u, v in [(i, j), (j, n - 1 - i), (n - 1 - i, n - 1 - j), (n - 1 - j, i)]:
                    matrix[u][v], val = val, matrix[u][v]

        if n % 2 == 1:
            j = (n - 1) // 2
            for i in range(n // 2):
                val = matrix[n - 1 - j][i]
                for u, v in [(i, j), (j, n - 1 - i), (n - 1 - i, n - 1 - j), (n - 1 - j, i)]:
                    matrix[u][v], val = val, matrix[u][v]