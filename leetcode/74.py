class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        rlo, rhi = 0, m - 1
        while rlo < rhi:
            mid = (rlo + rhi) // 2
            if target < matrix[mid][0]:
                rhi = mid
            elif target <= matrix[mid][-1]:
                rlo = mid
                break
            else:
                rlo = mid + 1

        clo, chi = 0, n - 1
        while clo <= chi:
            mid = (clo + chi) // 2
            if target == matrix[rlo][mid]:
                return True
            elif target < matrix[rlo][mid]:
                chi = mid - 1
            else:
                clo = mid + 1

        return False