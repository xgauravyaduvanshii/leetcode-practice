# LeetCode 2119. A Number After a Double Reversal — Easy
# https://leetcode.com/problems/a-number-after-a-double-reversal/
# Submission 2197613891 — Accepted, Python3
#
# My thinking: reversing a number drops its trailing
# zeros. A second reversal can only restore the
# original if nothing was lost — that happens when
# the number is 0 or does not end in 0.

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0
