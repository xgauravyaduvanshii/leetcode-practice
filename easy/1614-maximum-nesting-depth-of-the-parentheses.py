# LeetCode 1614. Maximum Nesting Depth of the Parentheses — Easy
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Submission 2197589407 — Accepted, Python3
#
# My thinking: I walk the string counting how deep
# I am — '(' goes one deeper, ')' comes back one.
# The deepest I ever get is the answer.

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        best = 0
        for ch in s:
            if ch == "(":
                depth += 1
                best = max(best, depth)
            elif ch == ")":
                depth -= 1
        return best
