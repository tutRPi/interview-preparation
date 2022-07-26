class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        groups = {}
        next_group = 1
        for i in range(len(isConnected)):
            if i not in groups:
                groups[i] = next_group
                next_group += 1

            for j in range(i):
                if isConnected[i][j] == 1:
                    if groups[i] != groups[j]:
                        self.join(i, j, groups)
            print(groups)

        return len(set(groups.values()))

    def join(self, i, j, groups):
        group1 = groups[i]
        group2 = groups[j]
        for k in groups:
            if groups[k] == group2:
                groups[k] = group1