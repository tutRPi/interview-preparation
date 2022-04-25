class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        num = gas[0] - cost[0]
        idx = 0
        for i in range(1, len(gas)):
            if num < 0:
                num = gas[i] - cost[i]
                idx = i
            else:
                num += gas[i] - cost[i]

        return idx if num >= 0 else -1