class Solution:
    def isHappy(self, n: int) -> bool:
        calculated_numbers = set()
        while n not in calculated_numbers:
            calculated_numbers.add(n)
            new_number = 0
            for digit in str(n):
                new_number += int(digit) ** 2

            if new_number == 1:
                return True

            n = new_number

        return False