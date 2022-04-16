class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        elif "1" <= s[0] <= "9":
            start = s.index("[")
            end = start + 1
            open_brackets = 1
            while open_brackets > 0:
                if s[end] == "]":
                    open_brackets -= 1
                elif s[end] == "[":
                    open_brackets += 1
                end += 1

            num = int(s[:start])
            return num * self.decodeString(s[start + 1: end - 1]) + self.decodeString(s[end:])
        else:
            # search first number, or end of line
            i = 0
            while i < len(s):
                if "1" <= s[i] <= "9":
                    break
                i += 1
            return s[:i] + self.decodeString(s[i:])
