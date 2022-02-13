# Sample Data: [15, 79, 25, 38, 69, 52, 58]
# Expected Result: [15, 25, 38, 52, 58, 69, 79]


def mergesort(a):
    arr = a.copy()
    if len(arr) <= 1:
        return arr

    m = int(len(arr) / 2)
    left = mergesort(arr[0:m])
    right = mergesort(arr[m:])
    res = []
    while len(left) > 0:
        if left[0] < right[0]:
            res.append(left[0])
            del left[0]
        else:
            res.append(right[0])
            del right[0]
    res.extend(left)
    res.extend(right)
    return res


x = [15, 79, 25, 38, 69, 52, 58]
assert mergesort(x) == [15, 25, 38, 52, 58, 69, 79]
