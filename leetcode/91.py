class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.get_decoding(s)

    def get_decoding(self, sub_string: str) -> int:
        if not sub_string:
            return 1

        if sub_string[0] == "0":
            return 0

        if len(sub_string) == 1:
            return 1

        if int(sub_string[:2]) > 26:
            return self.get_decoding(sub_string[1:])

        return self.get_decoding(sub_string[1:]) + self.get_decoding(sub_string[2:])


if __name__ == "__main__":
    assert Solution().numDecodings("") == 0
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("110") == 1
    assert Solution().numDecodings("27") == 1
    assert Solution().numDecodings("2101") == 1
    assert Solution().numDecodings("11106") == 2
    assert Solution().numDecodings("123123") == 9
    assert Solution().numDecodings("252353") == 4