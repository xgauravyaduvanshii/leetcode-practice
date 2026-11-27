# LeetCode 2310. Sum of Numbers With Units Digit K — Medium
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
# Submission 2204667817 — Accepted, Python3
#
# My thinking: if I use i numbers, their units digits add up to i*k, so
# the total's units digit must be (i*k) % 10 — which has to equal num's
# units digit, i.e. (num - i*k) % 10 == 0. I try i = 1..10 (ten numbers
# always suffice: adding ten more of the same units digit changes nothing
# mod 10), stopping early when i*k exceeds num, and return -1 if no i works.
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, 11):
            if i * k > num:
                break
            if (num - i * k) % 10 == 0:
                return i
        return -1
