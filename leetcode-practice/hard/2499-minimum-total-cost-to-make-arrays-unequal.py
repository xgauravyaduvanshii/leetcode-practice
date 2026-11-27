# LeetCode 2499. Minimum Total Cost to Make Arrays Unequal — Hard
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/
# Submission 2201781821 — Accepted, Python3
#
# My thinking: only the spots where the
# two arrays already match are broken —
# I pair those spots up, cheapest first.
# If one value fills more than half the
# broken spots, those spots cannot all be
# fixed among themselves, so I borrow
# good spots (two times the excess many),
# cheapest first, each one fitting neither
# side. With no dominant value the broken
# spots pair up on their own; when their
# count is odd the leftover borrows the
# cheapest fitting spot, good or already
# paired.

from collections import Counter


class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        bad = [i for i in range(n) if nums1[i] == nums2[i]]
        if not bad:
            return 0
        good = [i for i in range(n) if nums1[i] != nums2[i]]
        m = len(bad)
        cnt = Counter(nums1[i] for i in bad)
        val, mx = cnt.most_common(1)[0]
        total = sum(bad)

        def suitable_good(exclude_val):
            return [j for j in good if nums1[j] != exclude_val and nums2[j] != exclude_val]

        if mx > m // 2:
            need = 2 * mx - m
            cand = suitable_good(val)
            if len(cand) < need:
                return -1
            return total + sum(cand[:need])
        if m % 2 == 0:
            return total
        # odd count, no dominant value: one extra partner is needed
        extra = min(bad)
        for j in good:
            # j can partner a broken spot i when it fixes i and stays good
            if any(nums1[j] != nums2[i] and nums2[i] != nums2[j] for i in bad):
                extra = min(extra, j)
                break
        return total + extra
