class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dists = [[float('inf') if mat[i][j] == 1 else 0 for j in range(len(mat[0]))] for i in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dists[i][j] = min(dists[i][j], 1 + dists[max(0, i - 1)][j], 1 + dists[i][max(0, j - 1)])

        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[0]))):
                dists[i][j] = min(dists[i][j], 1 + dists[min(len(mat) - 1, i + 1)][j],
                                  1 + dists[i][min(len(mat[0]) - 1, j + 1)])

        return dists