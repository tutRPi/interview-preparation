class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            num = numbers[i]
            while l <= r:
                m = (l + r) // 2
                if num + numbers[m] == target:
                    return [i + 1, m + 1]

                if num + numbers[m] < target:
                    l = m + 1
                else:
                    r = m - 1