def dfs(board, visited, y, x, word):
    if word == "":
        return True
    for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= j < len(board) and 0 <= i < len(board[j]):
            if (i, j) not in visited:
                visited.append((i, j))
                if board[j][i] == word[0]:
                    if dfs(board, visited, j, i, word[1:]) is True:
                        return True
    return False


def word_search(board: list, word) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if dfs(board, [], i, j, word) is True:
                return True
    return False


if __name__ == "__main__":
    assert word_search([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ], "SAD") is True
    assert word_search([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ], "SAF") is False
