class Solution:

    def maxArea(self, height: List[int]) -> int:

        current_area = 0
        left, right = 0, len(height) - 1

        while left != right:

            area = (right - left) * min(height[left], height[right])
            if area > current_area:
                current_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return current_area