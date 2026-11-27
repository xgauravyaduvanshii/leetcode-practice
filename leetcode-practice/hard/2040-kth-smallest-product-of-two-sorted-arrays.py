# LeetCode 2040. Kth Smallest Product of Two Sorted Arrays — Hard
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
# Submission 2201556496 — Accepted, Python3
#
# My thinking: I guess a value and count how
# many pairs multiply to no more than it — a
# positive first number caps the second from
# above, a negative one from below — then I
# narrow the guess until the count reaches k.

import bisect


class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        m = len(nums2)

        def count_le(x):
            cnt = 0
            for a in nums1:
                if a > 0:
                    cnt += bisect.bisect_right(nums2, x // a)
                elif a < 0:
                    cnt += m - bisect.bisect_left(nums2, -(x // (-a)))
                else:
                    if x >= 0:
                        cnt += m
            return cnt

        lo, hi = -10**10 - 5, 10**10 + 5
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
