# LeetCode 2226. Maximum Candies Allocated to K Children — Medium
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
# Submission 2204509771 — Accepted, Python3
#
# My thinking: if I can give every child x candies, I can also give any
# smaller amount, so the best x is found by binary search. For a trial
# x I count how many piles of size x the piles can be split into,
# stopping early once I reach k.
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        lo, hi = 0, max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            total = 0
            for c in candies:
                total += c // mid
                if total >= k:
                    break
            if total >= k:
                lo = mid
            else:
                hi = mid - 1
        return lo
