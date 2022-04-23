class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        for i, n in enumerate(candidates):
            if n == target:
                results.append([n])
            elif n < target:
                others = self.combinationSum(candidates[i:], target - n)
                for arr in others:
                    results.append([n] + arr)
        return results
