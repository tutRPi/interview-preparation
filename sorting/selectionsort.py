# Sample Data: [14,46,43,27,57,41,45,21,70]
# Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]


def selectionsort(arr):
    for i in range(len(arr)):
        pos = i
        for j in range(i, len(arr)):
            if arr[pos] > arr[j]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]


x = [14, 46, 43, 27, 57, 41, 45, 21, 70]
selectionsort(x)
assert x == [14, 21, 27, 41, 43, 45, 46, 57, 70]
