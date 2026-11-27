# LeetCode 787. Cheapest Flights Within K Stops — Medium
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Submission 2198937535 — Accepted, Python3
#
# My thinking: with at most k stops I can take at
# most k + 1 flights, so I relax every flight that
# many rounds — the same idea as Bellman-Ford.
# Each round uses the previous round's prices so
# a single round never counts two flights.

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            new_prices = prices[:]
            for u, v, w in flights:
                if prices[u] != float("inf"):
                    new_prices[v] = min(new_prices[v], prices[u] + w)
            prices = new_prices
        return -1 if prices[dst] == float("inf") else prices[dst]
