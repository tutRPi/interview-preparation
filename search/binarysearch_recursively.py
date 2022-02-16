# binary_search([1,2,3,5,8], 6) -> False
# binary_search([1,2,3,5,8], 5) -> True

def binary_search(arr, x):
    if len(arr) == 0:
        return False

    mid = int(len(arr) / 2)
    if arr[mid] == x:
        return True
    elif arr[mid] < x:
        return binary_search(arr[mid + 1:], x)
    else:
        return binary_search(arr[:mid], x)


assert binary_search([1, 2, 3, 5, 8], 6) is False
assert binary_search([1, 2, 3, 5, 8], 5) is True
assert binary_search([1, 2, 3, 5, 8], 2) is True
assert binary_search([1, 2, 3, 5, 8], 4) is False

# complexity: O(log n)
