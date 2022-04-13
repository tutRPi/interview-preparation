class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()
                if op == "+":
                    stack.append(left + right)
                elif op == "-":
                    stack.append(left - right)
                elif op == "*":
                    stack.append(left * right)
                elif op == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(op))
        return stack[0]