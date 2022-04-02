class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacements = {}
        for i, c in enumerate(s):
            if c not in replacements:
                if t[i] in replacements.values():
                    return False
                replacements[c] = t[i]
            elif replacements[c] != t[i]:
                return False
        return True