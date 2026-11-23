# LeetCode 1954. Minimum Garden Perimeter to Collect Enough Apples — Medium
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
# Submission 2201865185 — Accepted, Python3
#
# My thinking: a square of radius n
# holds 2n(n+1)(2n+1) apples — the count
# grows with the cube of the radius, so
# I binary-search the smallest radius
# that gathers enough, and the fence is
# eight times that radius.

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def total(n: int) -> int:
            return 2 * n * (n + 1) * (2 * n + 1)

        lo, hi = 1, 100000
        while lo < hi:
            mid = (lo + hi) // 2
            if total(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1
        return 8 * lo
