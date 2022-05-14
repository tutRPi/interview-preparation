class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counts = self.count_letters(t)
        w_start, w_end = 0, len(s)

        left, right = 0, -1
        missing = len(t)
        while right < len(s):
            if missing == 0:
                if right - left < w_end - w_start:
                    w_start, w_end = left, right

                if s[left] in counts:
                    counts[s[left]] += 1
                    if counts[s[left]] > 0:
                        missing += 1
                left += 1
                while left < len(s) and (s[left] not in counts or counts[s[left]] < 0):
                    if s[left] in counts:
                        counts[s[left]] += 1
                    left += 1
            else:
                right += 1
                if right < len(s) and s[right] in counts:
                    counts[s[right]] -= 1
                    if counts[s[right]] >= 0:
                        missing -= 1

        if w_end == len(s):
            return ""
        else:
            return s[w_start: w_end + 1]

    def count_letters(self, s) -> dict:
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
        return counts