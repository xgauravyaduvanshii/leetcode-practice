# LeetCode 2116. Check if a Parentheses String Can Be Valid — Medium
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
# Submission 2204404914 — Accepted, Python3
#
# My thinking: the length must be even, otherwise it is impossible. I
# scan left to right treating every unlocked position as '(' and fail
# if the balance ever goes negative, which proves no assignment can
# work. Then I scan right to left treating every unlocked position as
# ')' and fail the same way. Passing both scans means a valid
# assignment exists.
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        bal = 0
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        bal = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return True
