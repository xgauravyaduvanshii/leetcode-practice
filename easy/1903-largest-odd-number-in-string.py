# LeetCode 1903. Largest Odd Number in String — Easy
# https://leetcode.com/problems/largest-odd-number-in-string/
# Submission 2197603926 — Accepted, Python3
#
# My thinking: the number has to end in an odd digit.
# I scan from the right for the first odd digit and
# keep everything up to it — that is the biggest
# odd prefix. If there is no odd digit at all, the
# answer is empty.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
