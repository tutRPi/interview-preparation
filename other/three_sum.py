# Given array nums of integers, find all unique triplets in the array which gives
# the sum of zero. Solution may not contain duplicate triplets

# this can be narrowed down to a two sum problem, if setting one of the values fixed
def two_sum(sorted_nums, target) -> list:
    hashmap = {}
    result = []
    for i, num in enumerate(sorted_nums):
        complement = target - num
        if complement not in hashmap:
            hashmap[num] = i
        else:
            result.append((num, complement))
    return result


def three_sum(nums) -> list:
    result = []
    if len(nums) < 3:
        return result
    nums = sorted(nums)

    for i in range(len(nums) - 2):
        num = nums[i]
        pairs = two_sum(nums[i + 1:], -num)
        for n1, n2 in pairs:
            if (num, min(n1, n2), max(n1, n2)) not in result:
                result.append((num, min(n1, n2), max(n1, n2)))

    return result


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, - 1, -4]) == [(-1, 0, 1), (-1, -1, 2)]
