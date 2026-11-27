# LeetCode 1529. Minimum Suffix Flips — Medium
# https://leetcode.com/problems/minimum-suffix-flips/
# Submission 2199869803 — Accepted, Python3
#
# My thinking: the string starts as all zeros,
# and every flip changes the whole suffix. So
# each time the target switches from 0 to 1 or
# back, that is exactly one more flip.

class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        current = "0"
        for ch in target:
            if ch != current:
                flips += 1
                current = ch
        return flips
