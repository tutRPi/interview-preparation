class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0

        # count all letters
        letter_count = {}
        for letter in s:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1

        all_above_k = True
        for letter in letter_count:
            if letter_count[letter] < k:
                all_above_k = False
                break

        if all_above_k:
            return len(s)

        for i in range(len(s)):
            if letter_count[s[i]] < k:
                left_length = self.longestSubstring(s[:i], k)
                right_length = self.longestSubstring(s[i + 1:], k)
                return max(left_length, right_length)