class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for h in height:
            if stack and h > stack[0]:
                left_height = stack[0]
                while stack:
                    t = stack.pop()
                    res += left_height - t
            stack.append(h)

        height = stack[::-1]
        stack = []
        for h in height:
            if stack and h >= stack[0]:
                left_height = stack[0]
                while stack:
                    t = stack.pop()
                    res += left_height - t
            stack.append(h)

        return res