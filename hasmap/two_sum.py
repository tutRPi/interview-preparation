# Find the sum of two numbers in an array
# naive approach: O(n^2)
# better approach: using hashmap
# example:
# nums = [8, 3, 4, 9, 5], sum = 9

def two_sum(nums, target) -> (int, int):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in hash_table:
            hash_table[nums[i]] = i
        else:
            return hash_table[complement], i
    return -1, -1


if __name__ == '__main__':
    assert two_sum([8, 3, 4, 9, 5], 9) == (2, 4)
