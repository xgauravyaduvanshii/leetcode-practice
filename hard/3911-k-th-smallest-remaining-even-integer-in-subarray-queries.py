# LeetCode 3911. K-th Smallest Remaining Even Integer in Subarray Queries — Hard
# https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/
# Submission 2203385533 — Accepted, Python3
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def kthRemainingInteger(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: the positive evens are 2, 4, 6, ...
        # and a query deletes only the even values inside
        # nums[l..r]. Collect those evens once, sorted,
        # together with their positions. For a query let
        # c(m) be how many of the deleted evens are at most
        # 2m — a bisect_right over the slice of evens whose
        # positions fall in [l, r], minus the slice's left
        # offset, since bisect_right returns an insertion
        # index, not a count. The remaining evens up to 2m
        # number m - c(m), which never decreases as m grows
        # (c grows by at most 1 per step) and climbs by
        # steps of 0 or 1, so it hits k exactly at some m.
        # That m lies between k and k plus the number of
        # deleted evens, so binary search that range for
        # the smallest m with m - c(m) >= k; the answer is
        # 2m.
        even_vals = [v for v in nums if v % 2 == 0]
        even_pos = [i for i, v in enumerate(nums) if v % 2 == 0]
        ans = []
        for l, r, k in queries:
            lo = bisect_left(even_pos, l)
            hi = bisect_right(even_pos, r)
            cnt = hi - lo
            a, b = k, k + cnt
            while a < b:
                mid = (a + b) // 2
                removed = bisect_right(even_vals, 2 * mid, lo, hi) - lo
                if mid - removed >= k:
                    b = mid
                else:
                    a = mid + 1
            ans.append(2 * a)
        return ans
