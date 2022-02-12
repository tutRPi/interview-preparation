# x = [3, 7, 1, 8, 2, 5, 9, 4, 6]
# quicksort(x)
# assert x == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def partition(arr, start, end) -> int:
    pivot = arr[end]  # last element
    p_index = start
    for j in range(start, end):
        if arr[j] <= pivot:
            arr[p_index], arr[j] = arr[j], arr[p_index]
            p_index += 1
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index


def quicksort(arr: list, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    if start > end:
        return arr

    p_index = partition(arr, start, end)
    quicksort(arr, start, p_index - 1)
    quicksort(arr, p_index + 1, end)


x = [3, 7, 1, 8, 2, 5, 9, 4, 6]
quicksort(x)
assert x == [1, 2, 3, 4, 5, 6, 7, 8, 9]
