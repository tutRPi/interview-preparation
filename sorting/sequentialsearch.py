# Sequential_Search([11,23,58,31,56,77,43,12,65,19],31) -> (True, 3)


# Solution


def sequential_search(arr, x):
    for (i, n) in enumerate(arr):
        if n == x:
            return True, i
    return False, -1


assert sequential_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31) == (True, 3)

# complexity: O(n)
