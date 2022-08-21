class Solution:
    def findNthDigit(self, n: int) -> int:
        exp = 1
        rest = n
        while rest > 0:
            x = 10 ** exp
            y = 10 ** (exp - 1)
            if rest < exp * x:
                num, pos = divmod(rest - 1, exp)
                num += y
                return int(str(num)[pos])

            else:
                rest -= (x - y) * exp
                exp += 1