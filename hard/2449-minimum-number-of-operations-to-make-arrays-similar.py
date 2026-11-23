# LeetCode 2449. Minimum Number of Operations to Make Arrays Similar — Hard
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
# Submission 2201748861 — Accepted, Python3
#
# My thinking: an operation moves two
# units and never changes a number's
# parity, so odds only ever become odds
# and evens only evens — I sort each
# parity group on its own, add up how
# much too much each side holds, and
# every two units of excess is one move.

class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        ans = 0
        for parity in (0, 1):
            a = sorted(x for x in nums if x % 2 == parity)
            b = sorted(x for x in target if x % 2 == parity)
            excess = sum(max(0, x - y) for x, y in zip(a, b))
            ans += excess // 2
        return ans
