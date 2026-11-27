# LeetCode 2034. Stock Price Fluctuation — Medium
# https://leetcode.com/problems/stock-price-fluctuation/
# Submission 2204373303 — Accepted, Python3
#
# My thinking: I keep a dict of the latest price per timestamp plus the
# newest timestamp, so current() is a dict lookup. For the max and min
# I push every update onto a max-heap and a min-heap and never delete
# from them; when I read the top I throw away entries whose price no
# longer matches the dict, which lazily discards all the stale
# overwritten prices.
from heapq import heappush, heappop

class StockPrice:
    def __init__(self):
        self.d = {}
        self.latest = 0
        self.maxh = []
        self.minh = []

    def update(self, timestamp: int, price: int) -> None:
        self.d[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heappush(self.maxh, (-price, timestamp))
        heappush(self.minh, (price, timestamp))

    def current(self) -> int:
        return self.d[self.latest]

    def maximum(self) -> int:
        while self.maxh[0][0] != -self.d[self.maxh[0][1]]:
            heappop(self.maxh)
        return -self.maxh[0][0]

    def minimum(self) -> int:
        while self.minh[0][0] != self.d[self.minh[0][1]]:
            heappop(self.minh)
        return self.minh[0][0]
