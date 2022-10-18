class Solution:
    @staticmethod
    def valid_edit(s1: str, s2: str) -> bool:
        if abs(len(s1) - len(s2)) > 1:
            return False
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        offset = 0
        changes = 0
        for i in range(len(s1)):
            if offset + changes > 1:
                return False
            if s1[i] == s2[i + offset]:
                continue
            else:
                if i + offset + 1 == len(s2):
                    return False
                if s1[i] == s2[i + offset + 1]:
                    offset += 1
                else:
                    changes += 1
        return (changes <= 1 and len(s1) == len(s2)) or (offset <= 1 and len(s1) + 1 == len(s2))




if __name__ == "__main__":
    assert Solution.valid_edit("pale", "ple") == True
    assert Solution.valid_edit("pales", "pale") == True
    assert Solution.valid_edit("pale", "bale") == True
    assert Solution.valid_edit("pale", "bake") == False
    assert Solution.valid_edit("pale", "paleee") == False