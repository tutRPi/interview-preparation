import math


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        if n > 0:
            ans[1] = 1

            for i in range(2, n + 1):
                lg = math.log(i, 2)
                if lg % 1 == 0.0:
                    ans[i] = 1
                else:
                    ans[i] = 1 + ans[i - 2 ** int(lg)]

        return ans