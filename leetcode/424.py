class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in s}
        res = 0

        left = 0
        most = 0
        for right in range(len(s)):
            c = s[right]
            counts[c] += 1
            most = max(most, counts[c])
            if right - left + 1 - most > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
