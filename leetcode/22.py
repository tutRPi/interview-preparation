class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(open_par, s):
            if len(s) > 2 * n or open_par < 0:
                return

            if open_par == 0 and len(s) == 2 * n:
                result.append(s)
                return

            dfs(open_par + 1, s + "(")
            dfs(open_par - 1, s + ")")

        result = []
        dfs(0, "")
        return result
