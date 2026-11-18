# LeetCode 2833. Furthest Point From Origin — Easy
# https://leetcode.com/problems/furthest-point-from-origin/
# Submission 2198418453 — Accepted, Python3
#
# My thinking: the L and R moves partly cancel each
# other out, leaving the net distance between them.
# Every blank move can then be spent in the same
# direction as that net distance, so it adds one
# each to how far I can get.

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count("L")
        right = moves.count("R")
        blank = moves.count("_")
        return abs(left - right) + blank
