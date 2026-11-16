# LeetCode 1122. Relative Sort Array — Easy
# https://leetcode.com/problems/relative-sort-array/
# Submission 2197558454 — Accepted, Python3
#
# My thinking: I give each value in arr2 its position
# as a rank. Then I sort arr1 by that rank — values
# that appear in arr2 come first, in arr2's order,
# and the rest (which have no rank) go at the end
# sorted by their own value.

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        order = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))
