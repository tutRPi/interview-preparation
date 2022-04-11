class Solution:
    def myPow(self, x: float, n: int) -> float:

        neg = True if n < 0 else False
        n = abs(n)

        result = 1
        if n % 2 == 1:
            result *= x
            n -= 1

        if n > 0:
            half = self.myPow(x, n / 2)
            result *= half * half

        return 1.0 / result if neg else result