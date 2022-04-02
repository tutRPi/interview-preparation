class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = {i: set() for i in range(9)}
        vertical = {i: set() for i in range(9)}
        box = {i: set() for i in range(9)}
        for i in range(9):  # vertical
            for j in range(9):  # horizontal
                n = board[i][j]
                if n == ".": continue
                if n in horizontal[i] or n in vertical[j] or \
                        n in box[3 * (i // 3) + (j // 3)]:
                    return False

                horizontal[i].add(n)
                vertical[j].add(n)
                box[3 * (i // 3) + (j // 3)].add(n)
        return True
