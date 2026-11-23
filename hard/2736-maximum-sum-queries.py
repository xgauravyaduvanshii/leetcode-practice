# LeetCode 2736. Maximum Sum Queries — Hard
# https://leetcode.com/problems/maximum-sum-queries/
# Submission 2201878484 — Accepted, Python3
#
# My thinking: a query only cares
# about points whose first number
# clears its bar, so I sweep the bar
# downward, dropping each point into a
# tree keyed by its second number the
# moment it qualifies — and the tree
# always knows the best sum waiting at
# or above any second number.

import bisect


class Solution:
    def maximumSumQueries(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums1)
        points = sorted(((nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(n)), reverse=True)
        order = sorted(range(len(queries)), key=lambda i: queries[i][0], reverse=True)
        vals = sorted(set(nums2))
        size = len(vals)
        # Fenwick tree for suffix maximum, indexed from the top down
        bit = [-1] * (size + 1)

        def bit_update(i, v):
            # i is 0-based from the top (largest nums2 first)
            i += 1
            while i <= size:
                if v > bit[i]:
                    bit[i] = v
                i += i & -i

        def bit_query(i):
            # max over positions [0, i] (0-based from the top)
            i += 1
            best = -1
            while i > 0:
                if bit[i] > best:
                    best = bit[i]
                i -= i & -i
            return best

        ans = [-1] * len(queries)
        p = 0
        for qi in order:
            x, y = queries[qi]
            while p < n and points[p][0] >= x:
                _, b, s = points[p]
                # position from the top: number of values > b
                idx = size - 1 - bisect.bisect_left(vals, b)
                bit_update(idx, s)
                p += 1
            # first value >= y from the top is at index (count of values >= y) - 1
            cnt = size - bisect.bisect_left(vals, y)
            if cnt > 0:
                ans[qi] = bit_query(cnt - 1)
        return ans
