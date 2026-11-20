# LeetCode 1590. Make Sum Divisible by P — Medium
# https://leetcode.com/problems/make-sum-divisible-by-p/
# Submission 2199886065 — Accepted, Python3
#
# My thinking: I need to remove a subarray
# whose sum has the same remainder as the
# total. Walking prefix remainders, the
# earliest matching one gives the shortest
# removal.

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0
        seen = {0: -1}
        prefix = 0
        best = len(nums)
        for i, value in enumerate(nums):
            prefix = (prefix + value) % p
            need = (prefix - total) % p
            if need in seen:
                best = min(best, i - seen[need])
            seen[prefix] = i
        return best if best < len(nums) else -1
