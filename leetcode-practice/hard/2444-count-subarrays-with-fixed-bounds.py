# LeetCode 2444. Count Subarrays With Fixed Bounds — Hard
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# Submission 2201745545 — Accepted, Python3
#
# My thinking: a fixed-bound subarray must
# contain both minK and maxK and nothing
# outside their range — I sweep the right
# end along, remembering where each bound
# was last seen and where the last
# out-of-range value fell, and every
# left end up to the nearer bound works.

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0
        last_min = -1
        last_max = -1
        last_bad = -1
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                last_bad = i
            if x == minK:
                last_min = i
            if x == maxK:
                last_max = i
            ans += max(0, min(last_min, last_max) - last_bad)
        return ans
