# LeetCode 2717. Semi-Ordered Permutation — Easy
# https://leetcode.com/problems/semi-ordered-permutation/
# Submission 2197820727 — Accepted, Python3
#
# My thinking: I move 1 to the front and n to the
# back, counting the swaps for each. If 1 starts to
# the right of n, moving 1 left first shifts n one
# place right, so I save one swap.

from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums.index(1)
        y = nums.index(n)
        ans = x + (n - 1 - y)
        if x > y:
            ans -= 1
        return ans
