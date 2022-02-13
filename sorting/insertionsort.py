# Sample Data: [14,46,43,27,57,41,45,21,70]
# Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]


def insertionsort(arr):
    if len(arr) <= 1:
        return

    for i in range(1, len(arr)):
        for curr in reversed(range(1, i+1)):
            if arr[curr] >= arr[curr - 1]:
                break
            else:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]


x = [14, 46, 43, 27, 57, 41, 45, 21, 70]
insertionsort(x)
assert x == [14, 21, 27, 41, 43, 45, 46, 57, 70]
