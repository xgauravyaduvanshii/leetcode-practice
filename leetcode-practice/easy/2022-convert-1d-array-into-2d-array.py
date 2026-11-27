# LeetCode 2022. Convert 1D Array Into 2D Array — Easy
# https://leetcode.com/problems/convert-1d-array-into-2d-array/
# Submission 2197609369 — Accepted, Python3
#
# My thinking: the reshape only works when the array
# has exactly m * n elements — otherwise the answer
# is an empty list. If it fits, I slice the array
# into m rows of n elements each.

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]
