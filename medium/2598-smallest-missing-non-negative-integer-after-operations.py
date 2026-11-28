# LeetCode 2598. Smallest Missing Non-negative Integer After Operations — Medium
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
# Submission 2205096230 — Accepted, Python3
#
# My thinking: adding or subtracting value never changes an
# element's remainder modulo value, so each element can only
# ever become numbers with its own remainder. The targets
# 0, 1, 2, ... consume remainders in turn — target m needs a
# still-unused element with remainder m % value, and there are
# m // value earlier targets sharing it. The first m that
# runs out of suppliers is the mex.
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        freq = Counter(x % value for x in nums)
        m = 0
        while True:
            if freq[m % value] <= m // value:
                return m
            m += 1
