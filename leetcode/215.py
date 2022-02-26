class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums = self.heapsort(nums)
        return nums[-k]

    def _build_max_heap(self, nums):
        for i in reversed(range(len(nums))):
            parent_index = int((i - 1) / 2)
            self._sift_down(nums, parent_index, len(nums) - 1)

    def _sift_down(self, nums, parent_index, max_index):
        left_child = 2 * parent_index + 1
        right_child = 2 * parent_index + 2

        swap_index = parent_index
        if left_child <= max_index and nums[left_child] > nums[swap_index]:
            swap_index = left_child
        if right_child <= max_index and nums[right_child] > nums[swap_index]:
            swap_index = right_child

        if swap_index == parent_index:
            return
        else:
            nums[parent_index], nums[swap_index] = nums[swap_index], nums[parent_index]
            self._sift_down(nums, swap_index, max_index)

    def heapsort(self, nums):
        self._build_max_heap(nums)

        for i in reversed(range(len(nums))):
            nums[0], nums[i] = nums[i], nums[0]
            self._sift_down(nums, 0, i - 1)
        return nums


if __name__ == "__main__":
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
