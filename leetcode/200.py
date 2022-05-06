class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        count = 0
        land = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == "1"]

        visited = set()
        for start in land:
            if start not in visited:
                count += 1
                # search neighbors
                stack = [start]
                while stack:
                    i, j = stack.pop()
                    if (i, j) in visited:
                        continue

                    visited.add((i, j))
                    for y, x in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                            continue
                        stack.append((y, x))

        return count