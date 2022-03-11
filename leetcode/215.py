class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:

        # two pointers left right
        left, right = 0, len(arr) - 1
        while left <= right:
            pos = self.sort_part(arr, left, right)
            if pos == len(arr) - k:
                return arr[pos]
            elif pos < len(arr) - k:
                left = pos + 1
            else:
                right = pos - 1
        return -1

    def sort_part(self, arr, left, right):
        pivot = arr[right]
        index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1
        arr[right], arr[index] = arr[index], arr[right]
        return index