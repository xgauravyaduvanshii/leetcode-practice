# LeetCode 3028. Ant on the Boundary — Easy
# https://leetcode.com/problems/ant-on-the-boundary/
# Submission 2198716700 — Accepted, Python3
#
# My thinking: I follow the ant's position step by
# step from zero and count every time it lands back
# on zero.

from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        count = 0
        for step in nums:
            position += step
            if position == 0:
                count += 1
        return count
