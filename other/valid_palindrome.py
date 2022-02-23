def valid_palindrome(search_string):
    for i in range(int(len(search_string) / 2 + 1)):
        if search_string[i] != search_string[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    assert valid_palindrome("racecar") is True
    assert valid_palindrome("otto") is True
    assert valid_palindrome("ottoo") is False
