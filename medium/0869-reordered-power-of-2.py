# LeetCode 869. Reordered Power of 2 — Medium
# https://leetcode.com/problems/reordered-power-of-2/
# Submission 2198958104 — Accepted, Python3
#
# My thinking: rearranging the digits does not
# change how many of each digit there are, so I
# compare the digit counts of n against every
# power of two.

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counts = Counter(str(n))
        power = 1
        while power <= 10 ** 9:
            if Counter(str(power)) == counts:
                return True
            power *= 2
        return False
