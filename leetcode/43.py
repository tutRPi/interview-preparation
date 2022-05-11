class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult = "0"
        for i, c in enumerate(reversed(num1)):
            res = "0"
            for _ in range(int(c)):
                res = self.add(res, num2)

            if res != "0":
                res += "0" * i

            mult = self.add(mult, res)

        return mult

    def add(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = ""
        carry = 0
        for i in range(max(l1, l2) + 1):
            n1 = int(num1[l1 - i - 1]) if i < l1 else 0
            n2 = int(num2[l2 - i - 1]) if i < l2 else 0
            n = n1 + n2 + carry
            carry = n // 10
            n = n % 10
            res += str(n)

        res = res[::-1]

        while len(res) > 1 and res[0] == "0":
            res = res[1:]

        return res
