# LeetCode 1927. Sum Game — Medium
# https://leetcode.com/problems/sum-game/
# Submission 2201636227 — Accepted, Python3
#
# My thinking: Bob only survives when the
# two halves can still be balanced — if the
# count of blanks is odd Alice moves last
# and breaks it for sure, and when it is
# even the starting gap has to match what
# the lopsided blanks can still swing.

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        sum1 = sum(int(c) for c in num[:n] if c != '?')
        sum2 = sum(int(c) for c in num[n:] if c != '?')
        cnt1 = num[:n].count('?')
        cnt2 = num[n:].count('?')
        if (cnt1 + cnt2) % 2 == 1:
            return True
        return (sum1 - sum2) != (cnt2 - cnt1) * 9 // 2
