# LeetCode 2064. Minimized Maximum of Products Distributed to Any Store — Medium
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
# Submission 2204392985 — Accepted, Python3
#
# My thinking: the answer is monotone in the cap m — if a cap works,
# any larger cap works too — so I binary-search the smallest workable
# cap. A cap m works when the total number of stores needed,
# sum ceil(q / m) over all quantities, fits in n.
class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        lo, hi = 1, max(quantities)

        def ok(m: int) -> bool:
            return sum((q + m - 1) // m for q in quantities) <= n

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
