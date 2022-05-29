class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [float('inf')] * n
        res[src] = 0

        for _ in range(k + 1):
            tmp = res.copy()

            for s, t, p in flights:
                tmp[t] = min(tmp[t], res[s] + p)

            res = tmp

        return res[dst] if res[dst] != float('inf') else -1