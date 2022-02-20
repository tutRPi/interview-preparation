# given two arrays A and B, check if they have any items in common

def mutual_items(arr1, arr2):
    hashset = set(arr1)
    for x in arr2:
        if x in hashset:
            return True
    return False


if __name__ == "__main__":
    assert mutual_items([1, 2, 3, 4], [5, 6, 7, 4]) is True
    assert mutual_items([1, 2, 3, 4], [5, 6, 7]) is False
