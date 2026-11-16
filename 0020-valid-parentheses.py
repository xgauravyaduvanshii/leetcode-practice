"""LeetCode 20. Valid Parentheses — Easy
https://leetcode.com/problems/valid-parentheses/
Submission 2197268513 — Accepted, 103/103 testcases, Python3
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
