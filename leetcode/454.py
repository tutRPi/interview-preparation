class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        left_pairs = {}
        right_pairs = {}

        n = len(nums1)
        for i in range(n):
            for j in range(n):
                num = nums1[i] + nums2[j]
                if num not in left_pairs:
                    left_pairs[num] = 1
                else:
                    left_pairs[num] += 1

        for i in range(n):
            for j in range(n):
                num = nums3[i] + nums4[j]
                if num not in right_pairs:
                    right_pairs[num] = 1
                else:
                    right_pairs[num] += 1

        counts = 0
        for num in left_pairs:
            if -num in right_pairs:
                counts += left_pairs[num] * right_pairs[-num]
        return counts