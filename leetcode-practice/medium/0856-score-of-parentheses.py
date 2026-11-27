# LeetCode 856. Score of Parentheses — Medium
# https://leetcode.com/problems/score-of-parentheses/
# Submission 2198956398 — Accepted, Python3
#
# My thinking: an empty pair scores 1, and a pair
# around something scores twice what is inside.
# I keep a stack of running totals — one per open
# bracket — and add them up as brackets close.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += max(2 * inner, 1)
        return stack[0]
