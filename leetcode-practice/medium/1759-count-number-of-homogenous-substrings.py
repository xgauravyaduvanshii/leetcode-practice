# LeetCode 1759. Count Number of Homogenous Substrings — Medium
# https://leetcode.com/problems/count-number-of-homogenous-substrings/
# Submission 2199928530 — Accepted, Python3
#
# My thinking: a run of n equal letters holds
# n times n plus one over two homogenous
# substrings. I measure each run once and add
# them up.

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        total = 0
        run = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                run += 1
            else:
                total = (total + run * (run + 1) // 2) % mod
                run = 1
        total = (total + run * (run + 1) // 2) % mod
        return total
