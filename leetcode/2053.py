class Solution:
    def kthDistinct(self, arr: list, k: int) -> str:

        pos = 0
        for i in range(len(arr)):
            if arr[i] not in arr[0:i] and arr[i] not in arr[i + 1:]:
                print(arr[i])
                pos += 1
                if pos == k:
                    return arr[i]
        return ""


if __name__ == "__main__":
    assert Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"
