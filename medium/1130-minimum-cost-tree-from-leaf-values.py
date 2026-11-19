# LeetCode 1130. Minimum Cost Tree From Leaf Values — Medium
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# Submission 2199003873 — Accepted, Python3
#
# My thinking: I merge the smallest leaves
# first, always pairing a leaf with the smaller
# of its two neighbours — that pairing is the
# cheapest place for it in the tree.

from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        total = 0
        for value in arr:
            while stack and stack[-1] <= value:
                mid = stack.pop()
                total += mid * min(stack[-1] if stack else float("inf"), value)
            stack.append(value)
        while len(stack) > 1:
            total += stack.pop() * stack[-1]
        return total
