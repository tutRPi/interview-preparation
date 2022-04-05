import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        occurences = {}
        for word in words:
            if word not in occurences:
                occurences[word] = 1
            else:
                occurences[word] += 1

        heap = [(-val, key) for key, val in occurences.items()]
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result