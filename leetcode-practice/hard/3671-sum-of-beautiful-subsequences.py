# LeetCode 3671. Sum of Beautiful Subsequences — Hard
# https://leetcode.com/problems/sum-of-beautiful-subsequences/
# Submission 2203027606 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def sumOfBeautifulSubsequences(self, nums: List[int]) -> int:
        # My thinking: the answer is the sum of the GCDs of all
        # strictly increasing subsequences, and every integer is the
        # sum of Euler's totient over its divisors, so a subsequence
        # with GCD g contributes phi(d) once for every d dividing g.
        # Swapping the sums, I only need, for each d, how many
        # strictly increasing subsequences use only multiples of d.
        # I group each number's scaled values by its divisors first
        # (walking nums once, in order, so each group's list keeps
        # the original order), then count increasing subsequences
        # per group with a Fenwick tree over the compressed values:
        # each value adds 1 plus all counts of smaller values seen
        # so far. Multiply each group's count by phi(d) and add up.
        if not nums:
            return 0
        max_v = max(nums)
        phi = list(range(max_v + 1))
        for i in range(2, max_v + 1):
            if phi[i] == i:
                for j in range(i, max_v + 1, i):
                    phi[j] -= phi[j] // i
        groups = {}
        for v in nums:
            d = 1
            while d * d <= v:
                if v % d == 0:
                    groups.setdefault(d, []).append(v // d)
                    if d * d != v:
                        groups.setdefault(v // d, []).append(d)
                d += 1
        ans = 0
        for d, vals in groups.items():
            ans = (ans + phi[d] * self._count_inc_subseq(vals)) % MOD
        return ans

    @staticmethod
    def _count_inc_subseq(vals: List[int]) -> int:
        uniq = sorted(set(vals))
        comp = {v: i + 1 for i, v in enumerate(uniq)}
        bit = [0] * (len(uniq) + 2)

        def query(i: int) -> int:
            s = 0
            while i > 0:
                s = (s + bit[i]) % MOD
                i -= i & -i
            return s

        def update(i: int, delta: int) -> None:
            while i < len(bit):
                bit[i] = (bit[i] + delta) % MOD
                i += i & -i

        total = 0
        for x in vals:
            idx = comp[x]
            new = (1 + query(idx - 1)) % MOD
            update(idx, new)
            total = (total + new) % MOD
        return total
