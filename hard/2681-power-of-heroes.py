# LeetCode 2681. Power of Heroes — Hard
# https://leetcode.com/problems/power-of-heroes/
# Submission 2201868945 — Accepted, Python3
#
# My thinking: once the strengths are
# sorted, every group is ruled by its
# biggest hero, and the smaller ones in
# between can join or stay home freely
# — so I sweep once, carrying forward
# the sum of every smaller hero times
# the ways it could have been chosen.

class Solution:
    def sumOfPower(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        prev = 0
        ans = 0
        for x in nums:
            ans = (ans + x * x % MOD * (x + prev)) % MOD
            prev = (2 * prev + x) % MOD
        return ans
