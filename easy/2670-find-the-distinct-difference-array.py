# LeetCode 2670. Find the Distinct Difference Array — Easy
# https://leetcode.com/problems/find-the-distinct-difference-array/
# Submission 2197814844 — Accepted, Python3
#
# My thinking: for each position I need the number
# of distinct values up to it and the number of
# distinct values after it. I precompute both with
# a forward pass and a backward pass, then take the
# difference at each spot.

from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        seen = set()
        for i, x in enumerate(nums):
            seen.add(x)
            pref[i] = len(seen)
        suff = [0] * (n + 1)
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(nums[i])
            suff[i] = len(seen)
        return [pref[i] - suff[i + 1] for i in range(n)]
