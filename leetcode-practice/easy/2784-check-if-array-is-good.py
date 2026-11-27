# LeetCode 2784. Check if Array is Good — Easy
# https://leetcode.com/problems/check-if-array-is-good/
# Submission 2198411170 — Accepted, Python3
#
# My thinking: a good array is just the numbers 1
# up to n-1 with n written twice, so I build that
# expected array from the biggest number I see and
# compare it with the sorted input. If they match
# exactly, the array is good.

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        base = list(range(1, n)) + [n, n]
        return sorted(nums) == base
