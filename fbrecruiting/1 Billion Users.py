import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
def exp_sum(arr, exp):
    result = 1
    for num in arr:
        result += num ** exp
    return result


def getBillionUsersDay(growthRates):
    # Write your code here
    left, right = 1, 2

    while left < right:
        right_result = exp_sum(growthRates, right)
        if right_result < 1000000000:
            left = right
            right = 2 * right
        else:
            if left + 1 == right:
                return right
            mid = (left + right) // 2
            mid_result = exp_sum(growthRates, mid)
            if mid_result < 1000000000:
                left = mid
            else:
                right = mid


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    test_1 = [1.1, 1.2, 1.3]
    expected_1 = 79
    output_1 = getBillionUsersDay(test_1)
    check(expected_1, output_1)

    test_2 = [1.01, 1.02]
    expected_2 = 1047
    output_2 = getBillionUsersDay(test_2)
    check(expected_2, output_2)

    # Add your own test cases here
