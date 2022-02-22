def island_count(grid) -> int:
    count = 0
    discovered = set({})
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) not in discovered and grid[row][col] == 1:
                queue = [(row, col)]
                while len(queue) > 0:
                    n_r, n_c = queue.pop(0)
                    discovered.add((n_r, n_c))
                    # top, right, bottom, left
                    for r, c in [(n_r - 1, n_c), (n_r, n_c + 1), (n_r + 1, n_c), (n_r, n_c - 1)]:
                        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                            if grid[r][c] == 1 and (r, c) not in discovered:
                                queue.append((r, c))
                count += 1
    return count


if __name__ == "__main__":
    # we have a n x m map with water/land.
    # land is connected left/right/up/down
    grid = [
        [0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    assert island_count(grid) == 4
