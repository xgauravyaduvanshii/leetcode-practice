# LeetCode 2048. Next Greater Numerically Balanced Number — Medium
# https://leetcode.com/problems/next-greater-numerically-balanced-number/
# Submission 2204378298 — Accepted, Python3
#
# My thinking: a number is balanced when every digit d in it appears
# exactly d times. Balanced numbers are rare and the next one above n
# is never far away, so I just count upward from n + 1 and test each
# candidate by comparing its digit frequencies with the digits
# themselves. The first one that passes is the answer.
from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = n + 1
        while True:
            c = Counter(str(x))
            if all(int(d) == k for d, k in c.items()):
                return x
            x += 1
