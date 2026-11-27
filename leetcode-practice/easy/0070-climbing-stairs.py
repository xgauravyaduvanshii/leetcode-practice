# LeetCode 70. Climbing Stairs — Easy
# https://leetcode.com/problems/climbing-stairs/
# Submission 2197282290 — Accepted, Python3
#
# My thinking: to reach step n I must come from step
# n-1 (one step) or step n-2 (two steps), so the
# number of ways is just the sum of those two.
# That is the Fibonacci pattern, so I keep only
# the last two counts and roll them forward.

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
