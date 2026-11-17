# LeetCode 2485. Find the Pivot Integer — Easy
# https://leetcode.com/problems/find-the-pivot-integer/
# Submission 2197792169 — Accepted, Python3
#
# My thinking: the sum of 1 to n is n(n+1)/2. A pivot
# x works exactly when that total is a perfect
# square — then x is its square root. I check that
# with integer arithmetic.

class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        x = int(total ** 0.5)
        return x if x * x == total else -1
