class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices1 = {}
        indices2 = {}
        common = []
        for i, e in enumerate(list1):
            indices1[e] = i
        for i, e in enumerate(list2):
            indices2[e] = i

        for k, v in indices1.items():
            if k in indices2:
                common.append((v + indices2[k], k))

        if not common:
            return []
        least_common = [common[0]]
        for i in range(1, len(common)):
            if common[i][0] < least_common[0][0]:
                least_common = [common[i]]
            elif common[i][0] == least_common[0][0]:
                least_common.append(common[i])
        return [s[1] for s in least_common]