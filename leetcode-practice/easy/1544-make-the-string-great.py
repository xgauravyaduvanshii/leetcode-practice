# LeetCode 1544. Make The String Great — Easy
# https://leetcode.com/problems/make-the-string-great/
# Submission 2197585248 — Accepted, Python3
#
# My thinking: a bad pair is two adjacent letters
# that are the same letter in opposite cases —
# their character codes differ by exactly 32. I
# keep a stack: when the new letter cancels the
# top one, I pop it; otherwise I push it on.

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
