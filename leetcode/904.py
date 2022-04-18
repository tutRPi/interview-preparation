class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        stack = []
        max_possible = 0
        bag1, bag2 = -1, -1
        for i in range(len(fruits)):
            if bag1 == -1:
                bag1 = fruits[i]
            elif bag2 == -1 and bag1 != fruits[i]:
                bag2 = fruits[i]
            elif fruits[i] != bag1 and fruits[i] != bag2:
                max_possible = max(max_possible, stack[-1][1] - stack[0][1] + 1)
                other = stack.pop()
                while stack and stack[-1][0] == other[0]:
                    other = stack.pop()

                stack = [other]
                if bag1 == other[0]: bag2 = fruits[i]
                if bag2 == other[0]: bag1 = fruits[i]

            stack.append((fruits[i], i))

        max_possible = max(max_possible, stack[-1][1] - stack[0][1] + 1)
        return max_possible