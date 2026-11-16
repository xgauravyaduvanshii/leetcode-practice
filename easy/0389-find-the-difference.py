# LeetCode 389. Find the Difference — Easy
# https://leetcode.com/problems/find-the-difference/
# Submission 2197469947 — Accepted, Python3
#
# My thinking: t is s with one extra letter. If I
# XOR every letter of both strings together, every
# letter that appears twice cancels out — and the
# one left over is the extra letter.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s + t:
            result ^= ord(ch)
        return chr(result)
