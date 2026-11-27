# LeetCode 1249. Minimum Remove to Make Valid Parentheses — Medium
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Submission 2199018347 — Accepted, Python3
#
# My thinking: I match brackets with a stack.
# A closing bracket with nothing to match is
# deleted on the spot, and whatever opening
# brackets are left unmatched at the end go too.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        for i, ch in enumerate(chars):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""
        for i in stack:
            chars[i] = ""
        return "".join(chars)
