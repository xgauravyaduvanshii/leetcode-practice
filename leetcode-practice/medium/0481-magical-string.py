# LeetCode 481. Magical String — Medium
# https://leetcode.com/problems/magical-string/
# Submission 2198822122 — Accepted, Python3
#
# My thinking: the string describes itself — each
# number says how many times the next digit repeats.
# I generate it by reading those run lengths in
# order, alternating 1 and 2, and count the ones in
# the first n characters.

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        s = [1, 2, 2]
        index = 2
        while len(s) < n:
            next_value = 3 - s[-1]
            s.extend([next_value] * s[index])
            index += 1
        return s[:n].count(1)
