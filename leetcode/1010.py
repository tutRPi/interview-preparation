class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        results = 0
        times = {}
        for t in time:
            t_mod = t % 60

            rest = (60 - t_mod) % 60
            if rest in times:
                results += times[rest]

            if t_mod not in times:
                times[t_mod] = 0
            times[t_mod] += 1
        return results