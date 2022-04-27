class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        all_elems = set(nums1).union(set(nums2))
        neg_elems = set(nums1).difference(set(nums2))
        neg_elems = neg_elems.union( set(nums2).difference(set(nums1)) )
        return all_elems.difference(neg_elems)