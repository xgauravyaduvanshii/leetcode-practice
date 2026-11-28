# LeetCode 2443. Sum of Number and Its Reverse — Medium
# https://leetcode.com/problems/sum-of-number-and-its-reverse/
# Submission 2204948354 — Accepted, Python3
#
# My thinking: try every x from 0 up to num; if x plus its
# digit-reversal equals num, the answer is yes. No x larger than
# num can work, so the scan is complete.
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for x in range(num + 1):
            rev = 0
            y = x
            while y:
                rev = rev * 10 + y % 10
                y //= 10
            if x + rev == num:
                return True
        return False
