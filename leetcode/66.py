class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i, rest = 1, 1
        while rest and i <= len(digits):
            rest = (digits[-i] + 1) // 10
            digits[-i] = (digits[-i] + 1) % 10

            i += 1

        if i > len(digits) and rest:
            digits.insert(0, 1)

        return digits