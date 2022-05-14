import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            self.min_heap.append(num)
        else:
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

            if len(self.min_heap) >= len(self.max_heap) + 1:
                heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
            if len(self.max_heap) >= len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -1 * self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()