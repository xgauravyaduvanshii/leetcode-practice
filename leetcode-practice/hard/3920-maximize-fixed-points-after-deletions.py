# LeetCode 3920. Maximize Fixed Points After Deletions — Hard
# https://leetcode.com/problems/maximize-fixed-points-after-deletions/
# Submission 2203399864 — Accepted, Python3
from typing import List


class Solution:
    def maxFixedPoints(self, nums: List[int]) -> int:
        # My thinking: suppose the fixed points we end up
        # with are at original indices i_1 < ... < i_m
        # with values v_t = nums[i_t]. The t-th fixed
        # point has new index v_t, so exactly v_t kept
        # elements sit before it: the t - 1 earlier fixed
        # points plus v_t - t + 1 fillers chosen from the
        # indices before it. That is possible exactly when
        # v_1 <= i_1 and, between consecutive fixed points,
        # the v_{t+1} - v_t - 1 new fillers fit in the
        # i_{t+1} - i_t - 1 slots between them. Writing
        # d_t = v_t - i_t, both conditions are d_t <= 0
        # and d_{t+1} <= d_t. So the answer is the longest
        # chain of points (v, d) with d <= 0, strictly
        # increasing v and non-increasing d. The index
        # order comes for free: v_j < v_i and d_j >= d_i
        # force j = v_j - d_j <= v_j - d_i < i. I sort
        # the points by value, query the best chain over
        # d' >= d in a Fenwick tree for suffix maxima
        # (reversed coordinate), and insert each value
        # group only after querying it, so equal values
        # never chain together.
        pts = [(v, v - i) for i, v in enumerate(nums) if v - i <= 0]
        if not pts:
            return 0
        pts.sort(key=lambda p: p[0])
        ds = sorted({d for _, d in pts})
        comp = {d: i + 1 for i, d in enumerate(ds)}
        m = len(ds)
        bit = [0] * (m + 2)

        def bit_update(i: int, v: int) -> None:
            while i <= m:
                if v > bit[i]:
                    bit[i] = v
                i += i & -i

        def bit_query(i: int) -> int:
            r = 0
            while i > 0:
                if bit[i] > r:
                    r = bit[i]
                i -= i & -i
            return r

        ans = 0
        idx = 0
        while idx < len(pts):
            j = idx
            while j < len(pts) and pts[j][0] == pts[idx][0]:
                j += 1
            pending = []
            for t in range(idx, j):
                d = pts[t][1]
                # Suffix max over d' >= d is a prefix max
                # over the reversed coordinate.
                chain = bit_query(m - comp[d] + 1) + 1
                if chain > ans:
                    ans = chain
                pending.append((d, chain))
            for d, chain in pending:
                bit_update(m - comp[d] + 1, chain)
            idx = j
        return ans
