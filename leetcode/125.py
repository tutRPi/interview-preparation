class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [c.lower() for c in s if "a" <= c.lower() <= "z" or "0" <= c <= "9"]
        i, j = 0, len(letters) - 1
        while i < j:
            if letters[i] != letters[j]:
                return False
            i += 1
            j -= 1
        return True