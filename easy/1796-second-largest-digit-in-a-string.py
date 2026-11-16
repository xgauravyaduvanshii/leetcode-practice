# LeetCode 1796. Second Largest Digit in a String — Easy
# https://leetcode.com/problems/second-largest-digit-in-a-string/
# Submission 2197598795 — Accepted, Python3
#
# My thinking: only distinct digits matter. I pull
# out every digit in the string, drop duplicates
# with a set, sort them from biggest to smallest,
# and take the second one. If there are fewer than
# two distinct digits, the answer is -1.

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted({int(ch) for ch in s if ch.isdigit()}, reverse=True)
        return digits[1] if len(digits) > 1 else -1
