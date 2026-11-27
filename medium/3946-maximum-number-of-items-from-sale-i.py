# LeetCode 3946. Maximum Number of Items From Sale I — Medium
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
# Submission 2204235481 — Accepted, Python3
#
# My thinking: buying the first copy of an item unlocks one free copy
# of every other item whose factor it divides, so a first copy is worth
# 1 plus that many free copies, while any extra copy of the same item
# is worth just 1. I run a 0/1 knapsack over the first copies, then
# spend whatever budget is left on extra copies of the cheapest item,
# since each extra copy costs the same no matter which item it is.

from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        factors = [item[0] for item in items]
        prices = [item[1] for item in items]

        # free_copies[i] = how many other items item i gives for free
        # when we buy at least one copy of it.
        free_copies = [0] * n
        for i in range(n):
            count = 0
            for j in range(n):
                if j != i and factors[j] % factors[i] == 0:
                    count += 1
            free_copies[i] = count

        cheapest_price = min(prices)

        # 0/1 knapsack over first copies: taking item i once costs
        # prices[i] and yields 1 + free_copies[i] copies in total.
        unreachable = -10 ** 9
        best_for_spent = [unreachable] * (budget + 1)
        best_for_spent[0] = 0
        for i in range(n):
            value = 1 + free_copies[i]
            cost = prices[i]
            for spent in range(budget, cost - 1, -1):
                if best_for_spent[spent - cost] != unreachable:
                    best_for_spent[spent] = max(
                        best_for_spent[spent],
                        best_for_spent[spent - cost] + value,
                    )

        # Extra copies only add 1 copy each, so the leftover budget
        # buys as many copies of the cheapest item as it can afford.
        answer = 0
        for spent in range(budget + 1):
            if best_for_spent[spent] != unreachable:
                extra_copies = (budget - spent) // cheapest_price
                answer = max(answer, best_for_spent[spent] + extra_copies)
        return answer
