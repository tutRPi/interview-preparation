class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_positions = {c: i for i, c in enumerate(s)}

        result = []
        start = 0
        while start < len(s):
            last = last_positions[s[start]]

            j = start
            while j < last:
                last = max(last, last_positions[s[j]])
                j += 1

            result.append(last - start + 1)
            start = last + 1

        return result