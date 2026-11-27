# LeetCode 241. Different Ways to Add Parentheses — Medium
# https://leetcode.com/problems/different-ways-to-add-parentheses/
# Submission 2198725669 — Accepted, Python3
#
# My thinking: every operator can be the last one
# evaluated, splitting the expression in two. I
# solve the left and right halves the same way and
# combine every pair of their results through that
# operator. With no operator left, the expression is
# just a number.

from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1 :])
                for a in left:
                    for b in right:
                        if char == "+":
                            results.append(a + b)
                        elif char == "-":
                            results.append(a - b)
                        else:
                            results.append(a * b)
        return results if results else [int(expression)]
