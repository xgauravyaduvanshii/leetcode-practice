# LeetCode 1801. Number of Orders in the Backlog — Medium
# https://leetcode.com/problems/number-of-orders-in-the-backlog/
# Submission 2199939220 — Accepted, Python3
#
# My thinking: buys wait in a max-heap and
# sells in a min-heap. Each new order eats
# into the best opposite orders first, and
# whatever is left joins its own heap.

import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        buys = []
        sells = []
        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0 and sells and sells[0][0] <= price:
                    sellPrice, sellAmount = heapq.heappop(sells)
                    matched = min(amount, sellAmount)
                    amount -= matched
                    sellAmount -= matched
                    if sellAmount > 0:
                        heapq.heappush(sells, (sellPrice, sellAmount))
                if amount > 0:
                    heapq.heappush(buys, (-price, amount))
            else:
                while amount > 0 and buys and -buys[0][0] >= price:
                    buyPrice, buyAmount = heapq.heappop(buys)
                    matched = min(amount, buyAmount)
                    amount -= matched
                    buyAmount -= matched
                    if buyAmount > 0:
                        heapq.heappush(buys, (buyPrice, buyAmount))
                if amount > 0:
                    heapq.heappush(sells, (price, amount))
        return sum(amount for _, amount in buys + sells) % mod
