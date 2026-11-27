# LeetCode 1221. Split a String in Balanced Strings — Easy
# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Submission 2197563823 — Accepted, Python3
#
# My thinking: I keep a running balance — R adds 1,
# L subtracts 1. Whenever the balance returns to
# zero, I have just finished a balanced piece, so
# I count it and start the next one.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for ch in s:
            balance += 1 if ch == "R" else -1
            if balance == 0:
                count += 1
        return count
