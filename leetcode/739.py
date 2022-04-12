class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        wait = [0] * n

        stack = [0]
        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                wait[index] = i - index
            stack.append(i)
        return wait
