# LeetCode 3072. Distribute Elements Into Two Arrays II — Hard
# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/
# Submission 2201921190 — Accepted, Python3
#
# My thinking: each step needs to know,
# for both arrays, how many of their
# numbers are bigger than the new one.
# I compress the values and keep a
# Fenwick tree per array, so each count
# is one prefix sum and each placement
# is one update. The tie-breaks follow
# the rules: bigger count wins, then
# the shorter array, then arr1.

from typing import List
import bisect


class Fenwick:
    def __init__(self, n: int):
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        bit = self.bit
        n = len(bit) - 1
        while i <= n:
            bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        n = len(vals)
        bit1, bit2 = Fenwick(n), Fenwick(n)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        bit1.add(rank[nums[0]], 1)
        bit2.add(rank[nums[1]], 1)
        for x in nums[2:]:
            # Numbers <= x sit at ranks up to bisect_right.
            r = bisect.bisect_right(vals, x)
            g1 = len(arr1) - bit1.sum(r)
            g2 = len(arr2) - bit2.sum(r)
            if g1 > g2 or (g1 == g2 and len(arr1) <= len(arr2)):
                arr1.append(x)
                bit1.add(rank[x], 1)
            else:
                arr2.append(x)
                bit2.add(rank[x], 1)
        return arr1 + arr2
