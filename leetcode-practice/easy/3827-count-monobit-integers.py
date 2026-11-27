# 3827. Count Monobit Integers (Easy)
# https://leetcode.com/problems/count-monobit-integers/
# Submission 2200069937 — Accepted, Python3
class Solution:
    def countMonobit(self, n: int) -> int:
        # My thinking: apart from zero, a monobit
        # number is all ones in binary — 1, 3, 7, 15
        # and so on. I just count how many of those
        # fit up to n, plus one for zero itself.
        count = 1
        value = 1
        while value <= n:
            count += 1
            value = value * 2 + 1
        return count
