# LeetCode 788. Rotated Digits — Medium
# https://leetcode.com/problems/rotated-digits/
# Submission 2198937844 — Accepted, Python3
#
# My thinking: a number is good when it rotates
# into a different valid number. Digits 3, 4 and 7
# break the rotation, and at least one of 2, 5, 6
# or 9 must appear for the result to change.

class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0
        for num in range(1, n + 1):
            text = str(num)
            if any(d in "347" for d in text):
                continue
            if any(d in "2569" for d in text):
                good += 1
        return good
