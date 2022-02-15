# binary_search([1,2,3,5,8], 6) -> False
# binary_search([1,2,3,5,8], 5) -> True

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    found = False
    while low != high and not found:
        mid = int((high + low) / 2)
        if arr[mid] == x:
            found = True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return found


assert binary_search([1, 2, 3, 5, 8], 6) == False
assert binary_search([1, 2, 3, 5, 8], 5) == True

# complexity: O(log n)
