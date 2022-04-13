class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            bouquets = self.find_bouquets(bloomDay, mid, k)
            print(mid, bouquets)
            if bouquets >= m:
                hi = mid
            else:
                lo = mid + 1
        return hi

    def find_bouquets(self, bloomDay: List[int], day: int, k: int) -> int:
        counter = 0
        last = -1
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                if last == -1:
                    last = i

                if i - last + 1 == k:
                    counter += 1
                    last = i + 1
            else:
                last = -1
        return counter