import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def get_increase(i):
            return (classes[i][1] - classes[i][0]) / (classes[i][1] ** 2 + classes[i][1])

        # max heap (multiplied by 1)
        increase = [(-1 * get_increase(i), i) for i in range(len(classes)) if classes[i][0] != classes[i][1]]
        heapq.heapify(increase)
        print(len(increase))

        while extraStudents > 0 and len(increase) >= 2:
            lowest_ratio, lowest_index = heapq.heappop(increase)
            next_ratio, next_index = increase[0]

            students = min(int(lowest_ratio / next_ratio), extraStudents)
            extraStudents -= students
            classes[lowest_index][0] += students
            classes[lowest_index][1] += students

            heapq.heappush(increase, (-1 * get_increase(lowest_index), lowest_index))

        if increase:
            classes[increase[0][1]][0] += extraStudents
            classes[increase[0][1]][1] += extraStudents

        return sum(c[0] / c[1] for c in classes) / len(classes)
