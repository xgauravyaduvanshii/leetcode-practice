# LeetCode 198. House Robber — Medium
# https://leetcode.com/problems/house-robber/
# Submission 2198443209 — Accepted, Python3
#
# My thinking: at each house I choose between
# skipping it or robbing it together with the best
# haul up to two houses back. I only need the last
# two answers, so two numbers carry the whole
# history forward.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1
