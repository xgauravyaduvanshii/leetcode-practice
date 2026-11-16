# LeetCode 2243. Calculate Digit Sum of a String — Easy
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Submission 2197284749 — Accepted, Python3 (Daily Challenge, 16 Nov 2026)
#
# My thinking: while the string is longer than k, I
# split it into chunks of k digits, add up the digits
# in each chunk, and join those sums together into a
# new string. Then I do the same thing again until
# the string is short enough.

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_parts = []
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                total = sum(int(digit) for digit in chunk)
                new_parts.append(str(total))
            s = "".join(new_parts)
        return s
