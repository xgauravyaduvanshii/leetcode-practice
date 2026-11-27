# LeetCode 1739. Building Boxes — Hard
# https://leetcode.com/problems/building-boxes/
# Submission 2201133760 — Accepted, Python3
#
# My thinking: I fill a full pyramid as high as it
# goes, then the leftover boxes form one more partial
# layer — the ground boxes are the pyramid's base plus
# the base of that partial layer.

class Solution:
    def minimumBoxes(self, n: int) -> int:
        # largest h with h(h+1)(h+2)/6 <= n
        lo, hi = 0, 10 ** 6
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * (mid + 1) * (mid + 2) // 6 <= n:
                lo = mid
            else:
                hi = mid - 1
        h = lo
        remaining = n - h * (h + 1) * (h + 2) // 6
        # largest k with k(k+1)/2 <= remaining
        lo, hi = 0, 10 ** 6
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * (mid + 1) // 2 <= remaining:
                lo = mid
            else:
                hi = mid - 1
        k = lo
        remaining -= k * (k + 1) // 2
        return h * (h + 1) // 2 + k + (1 if remaining > 0 else 0)
