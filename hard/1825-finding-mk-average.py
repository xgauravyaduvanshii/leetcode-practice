# LeetCode 1825. Finding MK Average — Hard
# https://leetcode.com/problems/finding-mk-average/
# Submission 2201184897 — Accepted, Python3
#
# My thinking: I keep the last m numbers in two
# Fenwick trees — one for how many of each value
# there are, one for their sums — so the average
# of the middle part is just the sum of the
# smallest m-k values minus the sum of the
# smallest k values.

from collections import deque

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        bitmask = 1 << self.n.bit_length()
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx + 1

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.window = deque()
        self.cnt = BIT(100000)
        self.sums = BIT(100000)

    def addElement(self, num: int) -> None:
        self.window.append(num)
        self.cnt.add(num, 1)
        self.sums.add(num, num)
        if len(self.window) > self.m:
            old = self.window.popleft()
            self.cnt.add(old, -1)
            self.sums.add(old, -old)

    def calculateMKAverage(self) -> int:
        if len(self.window) < self.m:
            return -1
        return (self._sum_smallest(self.m - self.k) - self._sum_smallest(self.k)) // (self.m - 2 * self.k)

    def _sum_smallest(self, t: int) -> int:
        if t == 0:
            return 0
        v = self.cnt.kth(t)
        c = self.cnt.sum(v - 1)
        s = self.sums.sum(v - 1)
        return s + (t - c) * v
