import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.get_permutation_of_arr(list(range(1, n + 1)), k)

    def get_permutation_of_arr(self, arr: List[int], k) -> str:
        if len(arr) == 0:
            return ""
        elif len(arr) == 1:
            return str(arr[0])

        fac = math.factorial(len(arr) - 1)
        index = (k - 1) // fac
        elem = arr.pop(index)
        return str(elem) + self.get_permutation_of_arr(arr, k - index * fac)
