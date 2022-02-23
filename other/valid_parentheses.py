def valid_parentheses(search_string) -> bool:
    stack = []
    for c in search_string:
        if c in ['(', '[']:
            stack.append(c)
        else:
            if c == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if c == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

    return len(stack) == 0


if __name__ == "__main__":
    assert valid_parentheses("string()") is True
    assert valid_parentheses("string([sadasd])") is True
    assert valid_parentheses("string([sadasd]))") is False
    assert valid_parentheses("string([sadasd))") is False
