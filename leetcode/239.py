import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        queue = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(queue)

        for i in range(k - 1, len(nums)):
            heapq.heappush(queue, (-nums[i], i))
            while i - k + 1 > queue[0][1]:
                heapq.heappop(queue)

            res.append(-queue[0][0])

        return res