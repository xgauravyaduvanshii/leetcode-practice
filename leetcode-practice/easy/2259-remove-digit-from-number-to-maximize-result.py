# LeetCode 2259. Remove Digit From Number to Maximize Result — Easy
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
# Submission 2197620524 — Accepted, Python3
#
# My thinking: I try removing each occurrence of the
# given digit in turn, and keep the biggest result
# I get.

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""
        for i, ch in enumerate(number):
            if ch == digit:
                cand = number[:i] + number[i + 1:]
                if cand > best:
                    best = cand
        return best
