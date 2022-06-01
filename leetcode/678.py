class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            if lo < 0:
                lo = 0

        return lo == 0
