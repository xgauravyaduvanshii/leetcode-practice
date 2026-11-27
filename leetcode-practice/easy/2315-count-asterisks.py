# LeetCode 2315. Count Asterisks — Easy
# https://leetcode.com/problems/count-asterisks/
# Submission 2197622797 — Accepted, Python3
#
# My thinking: asterisks between a pair of | bars
# don't count. I walk through the string, toggling
# an inside-bars flag at each |, and count only the
# asterisks seen outside bars.

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside = False
        for ch in s:
            if ch == '|':
                inside = not inside
            elif ch == '*' and not inside:
                count += 1
        return count
