# LeetCode 775. Global and Local Inversions — Medium
# https://leetcode.com/problems/global-and-local-inversions/
# Submission 2198932225 — Accepted, Python3
#
# My thinking: a local inversion is always global
# too, so the two counts can only match when no
# far-apart inversion exists — that is, when every
# number is at most one place away from where it
# belongs.

from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(num - i) <= 1 for i, num in enumerate(nums))
