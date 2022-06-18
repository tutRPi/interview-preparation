class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = defaultdict(int)
        for c in s1:
            counts[c] += 1

        for c in s2[:len(s1)]:
            if c in counts:
                counts[c] -= 1

        absum = sum(abs(x) for x in counts.values())

        for i in range(len(s1), len(s2)):
            prev_char = s2[i - len(s1)]
            next_char = s2[i]
            if absum == 0:
                return True
            if s2[i - len(s1)] in counts:
                absum += abs(counts[prev_char] + 1) - abs(counts[prev_char])
                counts[s2[i - len(s1)]] += 1
            if s2[i] in counts:
                absum += abs(counts[next_char] - 1) - abs(counts[next_char])
                counts[s2[i]] -= 1

        return absum == 0