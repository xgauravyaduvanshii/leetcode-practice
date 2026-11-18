# LeetCode 564. Find the Closest Palindrome — Hard
# https://leetcode.com/problems/find-the-closest-palindrome/
# Submission 2198663536 — Accepted, Python3
#
# My thinking: the closest palindrome almost always
# comes from mirroring the first half of the number,
# so I try that half, one below it and one above it.
# The only exceptions are the all-nines number just
# below and the 100...001 just above, so I add those
# two as well and pick the nearest, smallest on a tie.

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        value = int(n)
        candidates = set()
        candidates.add(10 ** (length - 1) - 1)
        candidates.add(10 ** length + 1)
        prefix = int(n[:(length + 1) // 2])
        for base in (prefix - 1, prefix, prefix + 1):
            half = str(base)
            if length % 2 == 0:
                pal = half + half[::-1]
            else:
                pal = half + half[-2::-1]
            candidates.add(int(pal))
        candidates.discard(value)
        return str(min(candidates, key=lambda x: (abs(x - value), x)))
