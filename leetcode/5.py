class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        stack = [(i, i) for i in range(n)] + [(i, i + 1) for i in range(n - 1) if s[i] == s[i + 1]]

        longest = ""
        while stack:
            begin, end = stack.pop()
            if end - begin + 1 > len(longest):
                longest = s[begin:end + 1]

            begin -= 1
            end += 1
            if begin >= 0 and end < n and s[begin] == s[end]:
                stack.append((begin, end))

        return longest