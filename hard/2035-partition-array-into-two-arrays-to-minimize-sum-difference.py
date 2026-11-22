# LeetCode 2035. Partition Array Into Two Arrays to Minimize Sum Difference — Hard
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
# Submission 2201555938 — Accepted, Python3
#
# My thinking: I split the array in half and
# list every subset sum of each half by how
# many numbers it takes, then pair the halves
# so their sums land as close to half the total
# as they can.

import bisect


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)

        def subset_sums(arr):
            d = {0: [0]}
            for x in arr:
                nd = {}
                for cnt, sums in d.items():
                    nd.setdefault(cnt, []).extend(sums)
                    nd.setdefault(cnt + 1, []).extend([s + x for s in sums])
                d = nd
            return d

        left = subset_sums(nums[:n])
        right = subset_sums(nums[n:])
        for cnt in right:
            right[cnt].sort()
        ans = float('inf')
        for cnt1, sums1 in left.items():
            cnt2 = n - cnt1
            if cnt2 not in right:
                continue
            sums2 = right[cnt2]
            for s1 in sums1:
                target = total / 2 - s1
                idx = bisect.bisect_left(sums2, target)
                for j in (idx - 1, idx):
                    if 0 <= j < len(sums2):
                        ans = min(ans, abs(total - 2 * (s1 + sums2[j])))
        return ans
