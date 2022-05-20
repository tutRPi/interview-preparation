class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        def dfs(cols, neg_diag, pos_diag):
            if len(cols) == n:
                sol = []
                for r in range(n):
                    c = cols[r]
                    s = "." * c + "Q" + "." * (n - c - 1)
                    sol.append(s)
                res.append(sol)
                return

            r = len(cols)
            for c in range(n):
                if c in cols or r - c in neg_diag or r + c in pos_diag:
                    continue
                cols.append(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)
                dfs(cols, neg_diag, pos_diag)
                cols.pop()
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)

        dfs([], set(), set())
        return res