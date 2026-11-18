# LeetCode 3000. Maximum Area of Longest Diagonal Rectangle — Easy
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
# Submission 2198714143 — Accepted, Python3
#
# My thinking: the longest diagonal wins, and ties
# go to the bigger area. I compare squared diagonals
# so I never need a square root, keeping the best
# diagonal and its area as I go.

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diagonal = -1
        best_area = 0
        for length, width in dimensions:
            diagonal = length * length + width * width
            area = length * width
            if diagonal > best_diagonal or (
                diagonal == best_diagonal and area > best_area
            ):
                best_diagonal = diagonal
                best_area = area
        return best_area
