import math


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count = min(
            self.swap(tops[0], tops, bottoms),
            self.swap(bottoms[0], tops, bottoms),
            self.swap(tops[0], bottoms, tops),
            self.swap(bottoms[0], bottoms, tops),
        )
        if count == math.inf:
            return -1
        return count

    def swap(self, value, line1, line2):
        count = 0
        for i in range(len(line1)):
            if line1[i] == value:
                continue
            elif line2[i] == value:
                count += 1
            else:
                return math.inf
        return count


assert Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]) == 2
