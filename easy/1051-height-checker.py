# LeetCode 1051. Height Checker — Easy
# https://leetcode.com/problems/height-checker/
# Submission 2197554785 — Accepted, Python3
#
# My thinking: the correct order is just the heights
# sorted. I compare the students' current order
# against that sorted order, position by position,
# and count how many are standing in the wrong spot.

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        return sum(1 for a, b in zip(heights, expected) if a != b)
