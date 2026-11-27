# LeetCode 2033. Minimum Operations to Make a Uni-Value Grid — Medium
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
# Submission 2204370909 — Accepted, Python3
#
# My thinking: adding or subtracting x can only change a value within
# its own remainder class mod x, so every cell must share the same
# remainder or the answer is -1. Once they do, the cheapest common
# target is the median of all the values, and each cell costs
# |value - median| / x operations.
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = [v for row in grid for v in row]
        if any(v % x != a[0] % x for v in a): return -1
        a.sort()
        m = a[len(a) // 2]
        return sum(abs(v - m) // x for v in a)
