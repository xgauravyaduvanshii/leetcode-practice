# LeetCode 3915. Maximum Sum of Alternating Subsequence With Distance at Least K — Hard
# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/
# Submission 2203395177 — Accepted, Python3
from typing import List


class FenwickMax:
    def __init__(self, n: int):
        self.n = n
        self.t = [0] * (n + 2)

    def update(self, i: int, v: int) -> None:
        t, n = self.t, self.n
        while i <= n:
            if v > t[i]:
                t[i] = v
            i += i & -i

    def query(self, i: int) -> int:
        r = 0
        t = self.t
        while i > 0:
            if t[i] > r:
                r = t[i]
            i -= i & -i
        return r


class Solution:
    def maxAlternatingSum(self, nums: List[int], k: int) -> int:
        # My thinking: up[i] is the best score of a valid
        # subsequence ending at i whose last step goes up
        # (or a single element, which has no last step yet),
        # and down[i] the same with the last step going
        # down. A length-1 subsequence can be extended in
        # either direction, so up[i] is nums[i] plus the
        # best down[j] over eligible j with nums[j] <
        # nums[i], and down[i] is nums[i] plus the best
        # up[j] over eligible j with nums[j] > nums[i];
        # either term is 0 when no such j exists, which
        # just starts a fresh length-1 subsequence at i.
        # An index j becomes eligible once i - j >= k, so
        # I insert j = i - k as i advances. Both "best
        # over smaller values" and "best over larger
        # values" are prefix maxima over the value axis
        # (the second one on a reversed index), which two
        # Fenwick trees answer in O(log V) each. The
        # answer is the best up[i] or down[i].
        n = len(nums)
        vmax = max(nums)
        bit_lo = FenwickMax(vmax)  # down[j] at value nums[j]
        bit_hi = FenwickMax(vmax)  # up[j] at reversed value
        ans = 0
        up = [0] * n
        down = [0] * n
        for i, x in enumerate(nums):
            if i - k >= 0:
                j = i - k
                bit_lo.update(nums[j], down[j])
                bit_hi.update(vmax - nums[j] + 1, up[j])
            up[i] = x + bit_lo.query(x - 1)
            down[i] = x + bit_hi.query(vmax - x)
            if up[i] > ans:
                ans = up[i]
            if down[i] > ans:
                ans = down[i]
        return ans
