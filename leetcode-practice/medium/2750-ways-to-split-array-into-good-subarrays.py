# LeetCode 2750. Ways to Split Array Into Good Subarrays — Medium
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/
# Submission 2198359696 — Accepted, Python3
#
# My thinking: a good split needs exactly one 1
# in every piece, so the 1s decide everything.
# With no 1 there is no way at all. Otherwise
# the cut between two neighbouring 1s can fall
# anywhere in the zeroes between them, and the
# choices for each gap multiply together.

from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        ones = [i for i, value in enumerate(nums) if value == 1]
        if not ones:
            return 0
        ways = 1
        for a, b in zip(ones, ones[1:]):
            ways = ways * (b - a) % mod
        return ways
