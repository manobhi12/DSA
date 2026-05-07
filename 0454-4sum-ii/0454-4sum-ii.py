from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):

        sum_map = defaultdict(int)


        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1

        count = 0

 
        for c in nums3:
            for d in nums4:

                target = -(c + d)

                count += sum_map[target]

        return count