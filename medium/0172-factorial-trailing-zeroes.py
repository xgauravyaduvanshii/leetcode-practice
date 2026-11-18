# LeetCode 172. Factorial Trailing Zeroes — Medium
# https://leetcode.com/problems/factorial-trailing-zeroes/
# Submission 2198436759 — Accepted, Python3
#
# My thinking: every trailing zero comes from a
# factor of 10, which needs one 2 and one 5 — and
# 2s are always plentiful, so I only count the 5s.
# The count is n divided by 5, plus n divided by
# 25, plus n divided by 125, and so on, because
# each higher power of 5 hides another 5 inside.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n //= 5
            count += n
        return count
