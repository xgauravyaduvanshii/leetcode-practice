# LeetCode 3569. Maximize Count of Distinct Primes After Split — Hard
# https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/
# Submission 2202851249 — Accepted, Python3
from typing import List
from collections import defaultdict
import bisect


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: "distinct prime values" means values that are
        # themselves prime numbers, not prime factors — a 4 counts
        # for nothing. For a split k, every distinct prime value
        # contributes 1 (it is on one side or the other), plus one
        # more when the split falls strictly between its first and
        # last occurrence. So the answer is the number of distinct
        # primes plus the largest number of first-to-last intervals
        # covering any split, which I keep in a lazy segment tree
        # while point updates move the interval ends.
        limit = 100000
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        n = len(nums)
        occ = defaultdict(list)
        for i, x in enumerate(nums):
            if is_prime[x]:
                bisect.insort(occ[x], i)
        seg = SegMax(n)
        distinct = 0
        for p, pos in occ.items():
            distinct += 1
            if len(pos) >= 2:
                seg.add(pos[0] + 1, pos[-1], 1)
        ans = []
        for idx, val in queries:
            old = nums[idx]
            if old != val:
                if is_prime[old]:
                    pos = occ[old]
                    if len(pos) >= 2:
                        seg.add(pos[0] + 1, pos[-1], -1)
                    pos.pop(bisect.bisect_left(pos, idx))
                    if not pos:
                        del occ[old]
                        distinct -= 1
                    elif len(pos) >= 2:
                        seg.add(pos[0] + 1, pos[-1], 1)
                nums[idx] = val
                if is_prime[val]:
                    if val in occ:
                        pos = occ[val]
                        if len(pos) >= 2:
                            seg.add(pos[0] + 1, pos[-1], -1)
                        bisect.insort(pos, idx)
                        if len(pos) >= 2:
                            seg.add(pos[0] + 1, pos[-1], 1)
                    else:
                        occ[val] = [idx]
                        distinct += 1
            ans.append(distinct + seg.query_max())
        return ans


class SegMax:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.maxv = [0] * (2 * self.N)
        self.lazy = [0] * (2 * self.N)

    def _push(self, node):
        if self.lazy[node]:
            for ch in (node * 2, node * 2 + 1):
                self.maxv[ch] += self.lazy[node]
                self.lazy[ch] += self.lazy[node]
            self.lazy[node] = 0

    def _add(self, node, l, r, ql, qr, val):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.maxv[node] += val
            self.lazy[node] += val
            return
        self._push(node)
        mid = (l + r) // 2
        self._add(node * 2, l, mid, ql, qr, val)
        self._add(node * 2 + 1, mid + 1, r, ql, qr, val)
        self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])

    def add(self, l, r, val):
        if l > r:
            return
        self._add(1, 0, self.N - 1, l, r, val)

    def query_max(self):
        return self.maxv[1]
