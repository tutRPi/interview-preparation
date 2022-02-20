# input: "DBCABA"
# output: "B" (or None if not found)
# naive approach: iterate through all -> O(n^2)
# with hash set: O(n)

def frc(search_string):
    hash_set = set({})
    for c in search_string:
        if c in hash_set:
            return c
        else:
            hash_set.add(c)
    return None


if __name__ == "__main__":
    assert frc("DBCABA") == "B"
    assert frc("ABCDEF") is None
