# LeetCode 921. Minimum Add to Make Parentheses Valid — Medium
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Submission 2198969815 — Accepted, Python3
#
# My thinking: I walk the string keeping the
# open brackets waiting for a match. A closing
# bracket with nothing open needs one added in
# front, and the opens left over at the end each
# need one behind.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        for ch in s:
            if ch == "(":
                open_needed += 1
            elif open_needed > 0:
                open_needed -= 1
            else:
                close_needed += 1
        return open_needed + close_needed
