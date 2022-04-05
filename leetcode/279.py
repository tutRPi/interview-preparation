import math

class Solution:
    def numSquares(self, n: int) -> int:
        counts = [i for i in range(n+1)]

        for i in range(n+1):
            j = 0
            while j*j <= i:
                counts[i] = min(counts[i], counts[i - j*j] + 1)
                j += 1
        return counts[-1]