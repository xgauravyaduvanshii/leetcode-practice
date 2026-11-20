# LeetCode 1712. Ways to Split Array Into Three Subarrays — Medium
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
# Submission 2199916525 — Accepted, Python3
#
# My thinking: for each left cut, the middle
# cut must keep the sums non-decreasing. Prefix
# sums turn those bounds into two binary
# searches, and I count the valid cuts between
# them.

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        total = prefix[n]
        count = 0
        for i in range(1, n - 1):
            left = prefix[i]
            if left * 3 > total:
                break
            lo = bisect_left(prefix, 2 * left, i + 1, n)
            hi = bisect_right(prefix, (total + left) // 2, i + 1, n) - 1
            if lo <= hi:
                count += hi - lo + 1
        return count % mod
