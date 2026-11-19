# LeetCode 1433. Check If a String Can Break Another String — Medium
# https://leetcode.com/problems/check-if-a-string-can-break-another-string/
# Submission 2199057230 — Accepted, Python3
#
# My thinking: with both strings sorted, one
# breaks the other when every letter of the
# first is at most — or at least — the letter
# across from it. I check both directions.

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        b = sorted(s2)
        return all(x <= y for x, y in zip(a, b)) or all(x >= y for x, y in zip(a, b))
