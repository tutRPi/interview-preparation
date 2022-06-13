class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n - 1):
            tmp = ""
            l, r = 0, 1
            curr = s[0]
            while r < len(s):
                if s[r] != curr:
                    tmp += str(r - l) + curr
                    curr = s[r]
                    l = r
                r += 1

            tmp += str(r - l) + curr
            s = tmp

        return s