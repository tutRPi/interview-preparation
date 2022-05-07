class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])

        positions = defaultdict(list)
        for i in range(N):
            for j in range(M):
                positions[board[i][j]].append((i, j))

        def dfs(i, j, next_char_pos, visited) -> bool:
            if (i, j) in visited or i < 0 or j < 0 or i >= N or j >= M or board[i][j] != word[next_char_pos]:
                return False

            if next_char_pos == len(word) - 1 and board[i][j] == word[next_char_pos]:
                return True

            visited.add((i, j))
            for u, v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (u, v) not in visited:
                    if dfs(u, v, next_char_pos + 1, visited):
                        return True
            visited.remove((i, j))

        for (i, j) in positions[word[0]]:
            if dfs(i, j, 0, set()):
                return True

        return False
