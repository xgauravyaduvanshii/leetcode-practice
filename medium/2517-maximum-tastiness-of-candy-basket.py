# LeetCode 2517. Maximum Tastiness of Candy Basket — Medium
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
# Submission 2204981660 — Accepted, Python3
#
# My thinking: sort the prices and binary-search the largest minimum
# difference d. To test d, greedily take the cheapest candy, then
# the next one at least d dearer, and so on — if k candies can be
# picked that way, d is achievable.
class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        price.sort()

        def feasible(d: int) -> bool:
            count = 1
            prev = price[0]
            for x in price[1:]:
                if x - prev >= d:
                    count += 1
                    prev = x
                    if count == k:
                        return True
            return count >= k

        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
