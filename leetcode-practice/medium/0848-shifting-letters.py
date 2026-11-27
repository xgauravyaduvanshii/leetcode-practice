# LeetCode 848. Shifting Letters — Medium
# https://leetcode.com/problems/shifting-letters/
# Submission 2198953559 — Accepted, Python3
#
# My thinking: every letter is shifted by its own
# amount plus all the shifts after it. I walk
# from the end, keeping a running total of those
# shifts modulo 26.

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        result = []
        for ch, shift in zip(reversed(s), reversed(shifts)):
            total = (total + shift) % 26
            result.append(chr((ord(ch) - ord("a") + total) % 26 + ord("a")))
        return "".join(reversed(result))
