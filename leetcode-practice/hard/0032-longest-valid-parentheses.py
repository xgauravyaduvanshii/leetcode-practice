# LeetCode 32. Longest Valid Parentheses — Hard
# https://leetcode.com/problems/longest-valid-parentheses/
# Submission 2198364337 — Accepted, Python3
#
# My thinking: I keep a stack of positions, starting
# with -1 as the floor. An opening bracket goes on
# the stack. A closing bracket pops one off — if the
# stack is empty afterwards, this closing bracket
# becomes the new floor; otherwise the distance from
# the current position back to the top of the stack
# is a valid stretch, and I keep the longest one.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        best = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])
        return best
