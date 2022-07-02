class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]

        for n in nums:
            l = len(sets)
            for i in range(l):
                sets.append(sets[i] + [n])
        return sets