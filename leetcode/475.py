class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters = list(set(heaters))
        heaters.sort()

        radius = 0
        j = 0
        for i in range(len(houses)):
            while j < len(heaters) - 1 \
                    and abs(houses[i] - heaters[j]) > abs(houses[i] - heaters[j + 1]):
                j += 1

            radius = max(radius, abs(houses[i] - heaters[j]))

        return radius