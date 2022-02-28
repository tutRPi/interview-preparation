class Solution:
    def getStrongest(self, arr: list, k: int) -> list:
        sorted_arr = sorted(arr)
        median = arr[int((len(arr) - 1) / 2)]

        strong_vals = [abs(n - median) for n in sorted_arr]
        output = []
        for i in range(k):
            if strong_vals[0] > strong_vals[-1]:
                output.append(sorted_arr[0])
                sorted_arr.pop(0)
                strong_vals.pop(0)
            else:
                output.append(sorted_arr[-1])
                sorted_arr.pop()
                strong_vals.pop()
        return output


if __name__ == "__main__":
    assert Solution().getStrongest([1, 2, 3, 4, 5], 2) == [5, 1]
    assert Solution().getStrongest([-3, -2, 2, 1, 7], 2) == [7, -3]
