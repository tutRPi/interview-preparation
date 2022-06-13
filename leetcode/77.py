class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k, res, [], 1)
        return res

    def backtrack(self, n, k, res, path, index):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n + 1):
            self.backtrack(n, k, res, path + [i], i + 1)