# LeetCode 1007. Minimum Domino Rotations For Equal Row — Medium
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# Submission 2198985431 — Accepted, Python3
#
# My thinking: the target value can only be one
# of the two numbers on the first domino. For
# each candidate I count how many flips make the
# top row match and how many make the bottom row
# match, and take the smaller.

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotations(target):
            top_swaps = bottom_swaps = 0
            for top, bottom in zip(tops, bottoms):
                if top != target and bottom != target:
                    return -1
                if top != target:
                    top_swaps += 1
                if bottom != target:
                    bottom_swaps += 1
            return min(top_swaps, bottom_swaps)

        result = rotations(tops[0])
        if result != -1:
            return result
        return rotations(bottoms[0])
