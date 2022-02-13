# Sample Data: [14,46,43,27,57,41,45,12,70]
# Expected Result: [12, 14, 27, 41, 43, 45, 46, 57, 70]


def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


x = [14, 46, 43, 27, 57, 41, 45, 12, 70]
print(bubble_sort(x))
assert bubble_sort(x) == [12, 14, 27, 41, 43, 45, 46, 57, 70]


# complexity: O(n^2)
