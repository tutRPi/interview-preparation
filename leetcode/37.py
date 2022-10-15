class Solution:
    def solveSudoku(self, board) -> bool:
        """
        Do not return anything, modify board in-place instead.
        """
        y, x = self.find_empty_cell(board)
        if y == -1:
            return True

        for n in range(1, 10):
            if self.is_valid(board, str(n), x, y):
                board[y][x] = str(n)

                if self.solveSudoku(board):
                    return True

                print("revert", y, x, n)
                board[y][x] = "."

        return False

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i, j
        return -1, -1

    def is_valid(self, board, number, x, y):
        # rows
        for i in range(9):
            if board[y][i] == number:
                return False

        # cols
        for i in range(9):
            if board[i][x] == number:
                return False

        o_x, o_y = x // 3, y // 3
        for i in range(3):
            for j in range(3):
                if board[3 * o_y + i][3 * o_x + j] == number:
                    return False

        return True
