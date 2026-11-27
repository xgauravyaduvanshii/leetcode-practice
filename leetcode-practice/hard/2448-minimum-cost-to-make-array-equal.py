# LeetCode 2448. Minimum Cost to Make Array Equal — Hard
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/
# Submission 2201746821 — Accepted, Python3
#
# My thinking: the cheapest target sits
# where the cost stops falling — the cost
# is convex, so I binary-search the point
# where making everything one bigger
# starts costing more than it saves.

class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        pairs = sorted(zip(nums, cost))

        def total(target):
            return sum(abs(x - target) * c for x, c in pairs)

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if total(mid) <= total(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        return total(lo)
