class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occ1 = {}
        occ2 = {}
        for n in nums1:
            if n not in occ1:
                occ1[n] = 1
            else:
                occ1[n] += 1
        for n in nums2:
            if n not in occ2:
                occ2[n] = 1
            else:
                occ2[n] += 1

        intersection = []
        for n in occ1:
            if n in occ2:
                for i in range(min(occ1[n], occ2[n])):
                    intersection.append(n)
        return intersection