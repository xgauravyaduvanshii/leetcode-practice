# LeetCode 638. Shopping Offers — Medium
# https://leetcode.com/problems/shopping-offers/
# Submission 2198889542 — Accepted, Python3
#
# My thinking: for whatever is still needed, I
# compare buying it all at list price against
# every special offer that fits, then solve the
# smaller remainder the same way. Memoising the
# remainders keeps the search fast.

from functools import lru_cache
from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def best(remaining):
            cost = sum(need * p for need, p in zip(remaining, price))
            for offer in special:
                new_remaining = tuple(r - o for r, o in zip(remaining, offer[:-1]))
                if all(x >= 0 for x in new_remaining):
                    cost = min(cost, offer[-1] + best(new_remaining))
            return cost

        return best(tuple(needs))
