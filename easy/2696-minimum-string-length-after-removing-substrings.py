# LeetCode 2696. Minimum String Length After Removing Substrings — Easy
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
# Submission 2197818551 — Accepted, Python3
#
# My thinking: I scan the string with a stack. When
# the top of the stack and the new character form
# "AB" or "CD", they cancel each other and I pop
# the stack; otherwise I push. What remains is the
# shortest possible string.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack and ((stack[-1] == 'A' and ch == 'B') or (stack[-1] == 'C' and ch == 'D')):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
