# LeetCode 1785. Minimum Elements to Add to Form a Given Sum — Medium
# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/
# Submission 2199934250 — Accepted, Python3
#
# My thinking: only the gap between the
# current sum and the goal matters, and every
# added element can cover at most the limit.
# The answer is the gap divided by the limit,
# rounded up.

from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(goal - sum(nums))
        return (diff + limit - 1) // limit
