# LeetCode 3768. Minimum Inversion Count in Subarrays of Fixed Length — Hard
# https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/
# Submission 2203169032 — Accepted, Python3
from typing import List


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix(self, i: int) -> int:
        # My thinking: sum of the frequencies at ranks 1..i.
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        # My thinking: slide a window of length k across nums
        # and keep its inversion count up to date with a
        # Fenwick tree over the compressed values. Dropping the
        # leftmost element x removes exactly the inversions it
        # formed with smaller elements still in the window;
        # adding a new rightmost element y adds exactly the
        # inversions it forms with larger elements already in
        # the window. Both updates are one Fenwick query each,
        # so every window costs O(log n) and the answer is the
        # smallest count seen.
        n = len(nums)
        ranks = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        bit = Fenwick(len(ranks))
        inv = 0
        for i in range(k):
            r = ranks[nums[i]]
            inv += i - bit.prefix(r)
            bit.add(r, 1)
        ans = inv
        for i in range(k, n):
            r_out = ranks[nums[i - k]]
            inv -= bit.prefix(r_out - 1)
            bit.add(r_out, -1)
            r_in = ranks[nums[i]]
            inv += (k - 1) - bit.prefix(r_in)
            bit.add(r_in, 1)
            ans = min(ans, inv)
        return ans
