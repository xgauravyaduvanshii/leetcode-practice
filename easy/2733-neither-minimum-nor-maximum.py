# LeetCode 2733. Neither Minimum nor Maximum — Easy
# https://leetcode.com/problems/neither-minimum-nor-maximum/
# Submission 2198357087 — Accepted, Python3
#
# My thinking: with fewer than three numbers there
# is no middle value at all. Otherwise I sort the
# numbers and the middle one is the second element.

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        return sorted(nums)[1]
