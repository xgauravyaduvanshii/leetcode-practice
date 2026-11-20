# LeetCode 1814. Count Nice Pairs in an Array — Medium
# https://leetcode.com/problems/count-nice-pairs-in-an-array/
# Submission 2199940666 — Accepted, Python3
#
# My thinking: a pair is nice exactly when
# the two numbers minus their reversals are
# equal. So I count how many times each such
# difference has appeared and add that each
# time I meet it again.

from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        counts = Counter()
        total = 0
        for num in nums:
            key = num - int(str(num)[::-1])
            total = (total + counts[key]) % mod
            counts[key] += 1
        return total
