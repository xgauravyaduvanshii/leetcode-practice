# LeetCode 3859. Count Subarrays With K Distinct Integers — Hard
# https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/
# Submission 2203316461 — Accepted, Python3
from typing import List


class _Fenwick:
    # Classic Fenwick tree over positions 0..n-1, with a
    # find_kth that returns the 0-based index whose prefix
    # sum first reaches the given 1-based rank.
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _prefix(self, idx: int) -> int:
        if idx < 0:
            return 0
        i = idx + 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def total(self) -> int:
        return self._prefix(self.n - 1)

    def find_kth(self, rank: int) -> int:
        idx = 0
        mask = 1 << self.n.bit_length()
        while mask:
            nxt = idx + mask
            if nxt <= self.n and self.bit[nxt] < rank:
                rank -= self.bit[nxt]
                idx = nxt
            mask >>= 1
        return idx


class Solution:
    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        # My thinking: fix the right end r and count the left
        # ends l whose window [l, r] has exactly k distinct
        # values, each appearing at least m times. Two
        # sliding windows give the l-range with exactly k
        # distinct values: l1 is the smallest l with at most
        # k distinct, l2 the smallest l with at most k - 1
        # distinct, so the distinct count is k exactly for
        # l1 <= l < l2. A value v has at least m occurrences
        # in [l, r] exactly when l is at or before q_v, the
        # position of its m-th occurrence from the right, so
        # the number of values with at least m occurrences in
        # [l, r] reaches k exactly when l is at or before the
        # k-th largest q_v among values seen at least m times
        # so far. A Fenwick tree over positions keeps those
        # q_v values and finds that k-th largest in O(log n),
        # and the valid l for this r are l1 through
        # min(l2 - 1, c), counted in O(1).
        n = len(nums)
        fw = _Fenwick(n)
        pos = {}
        freq1, freq2 = {}, {}
        d1 = d2 = 0
        l1 = l2 = 0
        ans = 0
        for r, v in enumerate(nums):
            lst = pos.setdefault(v, [])
            lst.append(r)
            j = len(lst)
            if j == m:
                fw.add(lst[0], 1)
            elif j > m:
                fw.add(lst[j - 1 - m], -1)
                fw.add(lst[j - m], 1)
            freq1[v] = freq1.get(v, 0) + 1
            if freq1[v] == 1:
                d1 += 1
            while d1 > k:
                u = nums[l1]
                freq1[u] -= 1
                if freq1[u] == 0:
                    d1 -= 1
                l1 += 1
            freq2[v] = freq2.get(v, 0) + 1
            if freq2[v] == 1:
                d2 += 1
            while d2 > k - 1:
                u = nums[l2]
                freq2[u] -= 1
                if freq2[u] == 0:
                    d2 -= 1
                l2 += 1
            tot = fw.total()
            if tot >= k:
                c = fw.find_kth(tot - k + 1)
                hi = min(l2 - 1, c)
                if hi >= l1:
                    ans += hi - l1 + 1
        return ans
