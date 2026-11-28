# LeetCode 2731. Movement of Robots — Medium
# https://leetcode.com/problems/movement-of-robots/
# Submission 2205216423 — Accepted, Python3
#
# My thinking: when two identical robots collide and bounce,
# the result is the same as if they passed straight through
# each other — only the multiset of positions matters. So move
# every robot d seconds in its own direction, sort the final
# positions, and sum the pairwise distances with the standard
# sorted-array formula, modulo 1e9+7.
class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        pos = sorted(x + d if ch == "R" else x - d for x, ch in zip(nums, s))
        n = len(pos)
        ans = 0
        for i, x in enumerate(pos):
            ans += x * (2 * i - n + 1)
        return ans % MOD
