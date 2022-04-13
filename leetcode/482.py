class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_s = "".join(s.split("-"))
        res = []
        while new_s:
            res.append(new_s[-k:].upper())
            new_s = new_s[:-k]
        return "-".join(res[::-1])
