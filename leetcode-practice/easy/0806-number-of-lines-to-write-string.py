# LeetCode 806. Number of Lines To Write String — Easy
# https://leetcode.com/problems/number-of-lines-to-write-string/
# Submission 2197529520 — Accepted, Python3
#
# My thinking: I write the letters one by one, keeping
# track of how full the current line is. If the
# next letter does not fit in the 100 pixels left,
# I start a new line with just that letter on it.
# At the end I know how many lines I used and how
# full the last one is.

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if current + w > 100:
                lines += 1
                current = w
            else:
                current += w
        return [lines, current]
