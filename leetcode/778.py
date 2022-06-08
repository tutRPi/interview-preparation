class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        min_val = max(grid[0][0], grid[n - 1][n - 1])
        max_val = n * n - 1

        res = max_val
        while min_val < max_val:
            mid = (min_val + max_val) // 2
            if self.has_path(grid, mid):
                res = mid
                max_val = mid
            else:
                min_val = mid + 1

        return res

    def has_path(self, grid: List[List[int]], num: int) -> int:
        n = len(grid)

        visited = set()
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()

            if (i, j) in visited or i < 0 or j < 0 or i >= n or j >= n or grid[i][j] > num:
                continue

            visited.add((i, j))

            if i == j == n - 1:
                return True

            for u, v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (u, v) not in visited:
                    stack.append((u, v))

        return False