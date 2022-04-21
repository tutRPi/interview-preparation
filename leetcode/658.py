class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]

        # find via binary search O(log(n))
        l, r = 0, len(arr) - 1
        closest = 0
        while l <= r:
            mid = (l + r) // 2
            if abs(arr[mid] - x) < abs(arr[closest] - x):
                closest = mid
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        # search k elements left and right O(k)
        i, j = closest, closest
        while j - i + 1 < k:
            if i == 0:
                j += 1
            elif j == len(arr) - 1:
                i -= 1
            elif abs(arr[j + 1] - x) < abs(arr[i - 1] - x):
                j += 1
            else:
                i -= 1

        return arr[i:j + 1]