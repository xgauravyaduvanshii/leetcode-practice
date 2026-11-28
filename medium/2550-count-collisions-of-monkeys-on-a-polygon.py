# LeetCode 2550. Count Collisions of Monkeys on a Polygon — Medium
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/
# Submission 2205060289 — Accepted, Python3
#
# My thinking: a collision is avoided only when every monkey
# moves the same way round — all clockwise or all
# counterclockwise. Out of 2^n direction choices, subtract those
# two, modulo 1_000_000_007.
class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, 1_000_000_007) - 2) % 1_000_000_007
