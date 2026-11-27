# LeetCode 2180. Count Integers With Even Digit Sum — Easy
# https://leetcode.com/problems/count-integers-with-even-digit-sum/
# Submission 2197616572 — Accepted, Python3
#
# My thinking: I go through every number from 1 to
# num, add up its digits, and count the ones whose
# digit sum is even.

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for x in range(1, num + 1):
            if sum(int(d) for d in str(x)) % 2 == 0:
                count += 1
        return count
