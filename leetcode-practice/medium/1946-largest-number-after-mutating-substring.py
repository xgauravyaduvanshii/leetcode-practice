# LeetCode 1946. Largest Number After Mutating Substring — Medium
# https://leetcode.com/problems/largest-number-after-mutating-substring/
# Submission 2201789763 — Accepted, Python3
#
# My thinking: I only ever want to
# change digits that grow — I walk from
# the left until I find the first digit
# the map improves, keep changing while
# the map does not shrink a digit, and
# stop the moment it would.

class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        digits = list(num)
        i = 0
        n = len(digits)
        while i < n and change[int(digits[i])] <= int(digits[i]):
            i += 1
        while i < n and change[int(digits[i])] >= int(digits[i]):
            digits[i] = str(change[int(digits[i])])
            i += 1
        return "".join(digits)
