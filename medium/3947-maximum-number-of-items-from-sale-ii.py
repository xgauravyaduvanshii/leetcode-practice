# LeetCode 3947. Maximum Number of Items From Sale II — Medium
# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/
# Submission 2204841052 — Accepted, Python3
#
# My thinking: buying a copy of an item can earn one free copy of a
# different item whose factor it divides, but only once per pair, so
# the first few copies of an item are worth 2 each (the copy itself
# plus one free copy) and every copy after that is worth just 1. I
# count, for each factor, how many items it can unlock for free, then
# buy the cheapest "worth 2" copies first — they only beat buying the
# cheapest item when their price is below twice the cheapest price —
# and spend whatever budget is left on copies of the cheapest item.

from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # factor_count[f] = how many items have factor f.
        factor_count = [0] * (n + 1)
        for factor, _price in items:
            factor_count[factor] += 1

        # unlocked_by[f] = how many items a factor f can give for free
        # (every item whose factor is a multiple of f, including itself).
        unlocked_by = [0] * (n + 1)
        for factor in range(1, n + 1):
            if factor_count[factor]:
                total = 0
                for multiple in range(factor, n + 1, factor):
                    total += factor_count[multiple]
                unlocked_by[factor] = total

        cheapest_price = min(price for _factor, price in items)

        # Each item's first (unlocked_by[factor] - 1) copies are worth 2
        # (minus 1 because an item cannot unlock a free copy of itself),
        # so I list those boosted copies as (price, count) pairs, cheapest
        # first, and only take ones cheaper than two cheapest copies.
        boosted = sorted(
            (price, unlocked_by[factor] - 1) for factor, price in items
        )

        remaining = budget
        total = 0
        boost_limit = 2 * cheapest_price
        for price, boosted_copies in boosted:
            if price >= boost_limit:
                break
            if boosted_copies <= 0:
                continue
            if remaining < price:
                break
            take = min(boosted_copies, remaining // price)
            total += 2 * take
            remaining -= take * price

        # Every copy after the boosted ones is worth just 1, so the
        # leftover budget buys as many copies of the cheapest item
        # as it can afford.
        total += remaining // cheapest_price
        return total
