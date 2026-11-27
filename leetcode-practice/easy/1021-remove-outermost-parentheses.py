# LeetCode 1021. Remove Outermost Parentheses — Easy
# https://leetcode.com/problems/remove-outermost-parentheses/
# Submission 2197551520 — Accepted, Python3
#
# My thinking: I track how deep I am inside
# parentheses. An opening bracket at depth 0 is
# the outermost one, so I skip it; a closing
# bracket that brings me back to depth 0 is also
# outermost, so I skip that too. Everything in
# between gets kept.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(ch)
        return "".join(result)
