# LeetCode 3624. Number of Integers With Popcount-Depth Equal to K II — Hard
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/
# Submission 2202886510 — Accepted, Python3
from typing import List


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self._sum(r) - (self._sum(l - 1) if l > 0 else 0)


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: the popcount-depth of a number up to 10^15
        # is at most 4, so every value falls into one of six depth
        # classes. I keep one Fenwick tree per depth, so a range
        # query is a single range sum on the tree for k, and an
        # update just moves one index between two trees. A query
        # for k = 5 always answers 0, since no number here reaches
        # depth 5.
        def depth(x):
            d = 0
            while x != 1:
                x = bin(x).count("1")
                d += 1
            return d

        n = len(nums)
        bits = [Fenwick(n) for _ in range(6)]
        depths = [depth(x) for x in nums]
        for i, d in enumerate(depths):
            bits[d].add(i, 1)
        ans = []
        nums = list(nums)
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                ans.append(bits[k].range_sum(l, r) if 0 <= k < 6 else 0)
            else:
                _, idx, val = q
                old = depths[idx]
                new = depth(val)
                if old != new:
                    bits[old].add(idx, -1)
                    bits[new].add(idx, 1)
                    depths[idx] = new
                nums[idx] = val
        return ans
