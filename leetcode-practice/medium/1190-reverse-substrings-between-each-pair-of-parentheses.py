# LeetCode 1190. Reverse Substrings Between Each Pair of Parentheses — Medium
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# Submission 2199009709 — Accepted, Python3
#
# My thinking: I keep a stack of the text built
# so far. An opening bracket starts a fresh
# piece, and a closing bracket flips that piece
# back onto the one below it.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for ch in s:
            if ch == "(":
                stack.append("")
            elif ch == ")":
                top = stack.pop()
                stack[-1] += top[::-1]
            else:
                stack[-1] += ch
        return stack[0]
