# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum
# Bruteforce would be O(n^2)
# Solution: Kadane's Algorithm
# sliding window, update global sum if current sum (=subarray) is greater

def maximum_subarray(nums: list) -> list:
    if not nums:
        return []

    global_array = [nums[0]]
    current_array = [nums[0]]
    for i in range(1, len(nums)):
        if sum(current_array + [nums[i]]) > nums[i]:
            current_array.append(nums[i])
        else:
            current_array = [nums[i]]

        if sum(current_array) > sum(global_array):
            global_array = current_array.copy()
    return global_array


if __name__ == "__main__":
    assert maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]
