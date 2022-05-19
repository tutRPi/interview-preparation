class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        start, end = newInterval
        res = []

        s = 0
        while s < len(intervals) and start > intervals[s][1]:
            res.append(intervals[s])
            s += 1

        e = s
        while e < len(intervals) and end >= intervals[e][0]:
            e += 1

        if s == e == 0 and end < intervals[0][0]:
            res = [newInterval] + intervals
        elif s == len(intervals):
            res.append(newInterval)
        elif e == len(intervals):
            res.append([min(intervals[s][0], start), max(intervals[-1][1], end)])
        else:
            if end < intervals[s][0]:
                res = res + [newInterval] + intervals[s:]
            elif end < intervals[e][0]:
                res = res + [[min(intervals[s][0], start), max(intervals[e - 1][1], end)]] + intervals[e:]
            else:
                res = res + [[min(intervals[s][0], start), max(intervals[e][1], end)]] + intervals[e + 1:]

        return res