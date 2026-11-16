# LeetCode 434. Number of Segments in a String — Easy
# https://leetcode.com/problems/number-of-segments-in-a-string/
# Submission 2197475723 — Accepted, Python3
#
# My thinking: a segment is just a run of characters
# with no spaces. Python's split() already breaks
# the string on any run of whitespace, so the number
# of pieces it gives me is the number of segments.

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
