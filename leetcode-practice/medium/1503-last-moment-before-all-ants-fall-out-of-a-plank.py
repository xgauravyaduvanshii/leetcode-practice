# LeetCode 1503. Last Moment Before All Ants Fall Out of a Plank — Medium
# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
# Submission 2199865130 — Accepted, Python3
#
# My thinking: ants passing through each other
# look the same as ants bouncing off, so each
# ant just walks straight off. The last one out
# is the farthest left-moving ant from the
# left edge, or the farthest right-moving ant
# from the right edge.

from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))
