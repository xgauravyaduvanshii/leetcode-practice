# LeetCode 2278. Percentage of Letter in String — Easy
# https://leetcode.com/problems/percentage-of-letter-in-string/
# Submission 2197621276 — Accepted, Python3
#
# My thinking: I count how many times the letter
# appears, multiply by 100 and divide by the
# string's length, rounding down.

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
