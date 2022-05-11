class Solution:
    def reverseBits(self, n: int) -> int:
        s = "0" * 32 + str(bin(n))
        s = s[-32:]
        res = 0
        for c in reversed(s):
            res = res << 1
            if c == "1":
                res = res | 1
        return res