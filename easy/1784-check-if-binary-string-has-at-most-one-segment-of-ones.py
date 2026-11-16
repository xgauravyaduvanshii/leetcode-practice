# LeetCode 1784. Check if Binary String Has at Most One Segment of Ones — Easy
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Submission 2197597841 — Accepted, Python3
#
# My thinking: two separate groups of ones always
# show up as a "01" — a zero followed later by a
# one. If the string has no "01" in it, all the
# ones form a single block (or there are none).

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
