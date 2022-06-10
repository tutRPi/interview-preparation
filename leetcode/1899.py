class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        exact = [set(), set(), set()]
        greater = set()

        for i in range(len(triplets)):
            for j in range(3):
                if triplets[i][j] == target[j]:
                    exact[j].add(i)
                elif triplets[i][j] > target[j]:
                    greater.add(i)

        for j in range(3):
            exact[j] = exact[j] - greater

        return min(len(exact[0]), len(exact[1]), len(exact[2])) > 0