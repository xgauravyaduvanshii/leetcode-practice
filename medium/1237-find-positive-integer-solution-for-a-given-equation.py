# LeetCode 1237. Find Positive Integer Solution for a Given Equation — Medium
# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
# Submission 2197564479 — Accepted, Python3
#
# My thinking: f grows when either input grows, so I
# can walk it like a staircase. I start at the
# top-left (x = 1, y = 1000). If f is too small, x
# must go up; if too big, y must come down. When
# f equals z I record the pair and step both ways
# at once — the next match can only be down-right
# from there.

class Solution:
    def findSolution(self, customfunction, z: int) -> list[list[int]]:
        result = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            value = customfunction.f(x, y)
            if value == z:
                result.append([x, y])
                x += 1
                y -= 1
            elif value < z:
                x += 1
            else:
                y -= 1
        return result
