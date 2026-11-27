# LeetCode 1015. Smallest Integer Divisible by K — Medium
# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Submission 2198986678 — Accepted, Python3
#
# My thinking: I build the number 1, 11, 111 and
# so on, tracking only the remainder. If k ends
# in 2 or 5 no repunit can ever divide it; if the
# remainders run out without hitting zero, the
# answer does not exist.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
