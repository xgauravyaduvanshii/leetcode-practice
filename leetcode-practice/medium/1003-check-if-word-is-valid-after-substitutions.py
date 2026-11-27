# LeetCode 1003. Check If Word Is Valid After Substitutions — Medium
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Submission 2198983460 — Accepted, Python3
#
# My thinking: I read the word left to right and
# stack the letters. Whenever the top three form
# "abc", they cancel out — a valid word leaves
# nothing on the stack.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ["a", "b", "c"]:
                del stack[-3:]
        return not stack
