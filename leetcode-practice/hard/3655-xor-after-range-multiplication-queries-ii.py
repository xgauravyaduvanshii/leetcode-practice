# LeetCode 3655. XOR After Range Multiplication Queries II — Hard
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/
# Submission 2202933133 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # My thinking: every query only multiplies, so the order of
        # the queries does not matter — each position ends up as
        # nums[i] times the product of the v's of the queries that
        # touch it. For a big step k there are only a few touched
        # positions, so I update them directly. For a small step k
        # I group the queries by k and use a difference array along
        # each residue class: multiply at the first touched index
        # and by the modular inverse just past the last one, then
        # one sweep carries the running product down each chain.
        n = len(nums)
        mult = [1] * n
        B = 350
        by_k = {}
        for l, r, k, v in queries:
            by_k.setdefault(k, []).append((l, r, v))
        for k, qs in by_k.items():
            if k > B:
                for l, r, v in qs:
                    i = l
                    while i <= r:
                        mult[i] = mult[i] * v % MOD
                        i += k
            else:
                diff = [1] * (n + 1)
                for l, r, v in qs:
                    diff[l] = diff[l] * v % MOD
                    e = l + (r - l) // k * k
                    if e + k < n:
                        diff[e + k] = diff[e + k] * pow(v, MOD - 2, MOD) % MOD
                cur = [1] * k
                for i in range(n):
                    cur[i % k] = cur[i % k] * diff[i] % MOD
                    mult[i] = mult[i] * cur[i % k] % MOD
        ans = 0
        for i in range(n):
            ans ^= nums[i] * mult[i] % MOD
        return ans
