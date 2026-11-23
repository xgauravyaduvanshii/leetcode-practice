# LeetCode 2426. Number of Pairs Satisfying Inequality — Hard
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
# Submission 2201732898 — Accepted, Python3
#
# My thinking: the condition is really
# about one number per index, d[i] = a[i]
# - b[i] — I walk from the right keeping
# the differences I have seen in a sorted
# list, and count how many of them are
# big enough to pair with the one I am on.

import bisect


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        d = [a - b for a, b in zip(nums1, nums2)]
        seen = []
        ans = 0
        for x in reversed(d):
            idx = bisect.bisect_left(seen, x - diff)
            ans += len(seen) - idx
            bisect.insort(seen, x)
        return ans
