# LeetCode 1967. Number of Strings That Appear as Substrings in Word — Easy
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Submission 2197606417 — Accepted, Python3
#
# My thinking: I just count how many of the patterns
# appear somewhere inside the word.

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum(1 for p in patterns if p in word)
