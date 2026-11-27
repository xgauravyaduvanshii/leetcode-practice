# LeetCode 2549. Count Distinct Numbers on Board — Easy
# https://leetcode.com/problems/count-distinct-numbers-on-board/
# Submission 2197801311 — Accepted, Python3
#
# My thinking: starting from n, the board eventually
# collects every number from 2 to n — that is n-1
# distinct numbers. The only exception is n = 1,
# where only the number 1 itself is ever on the
# board.

class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1
