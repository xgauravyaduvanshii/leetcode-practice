# LeetCode 2336. Smallest Number in Infinite Set — Medium
# https://leetcode.com/problems/smallest-number-in-infinite-set/
# Submission 2200984164 — Accepted, Python3
#
# My thinking: the smallest number is usually just the
# next one I have never handed out, unless a smaller
# number was added back — so I keep the added-back ones
# in a heap and the untouched ones in a counter.

import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.next = 1
        self.added_back = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.in_heap.discard(smallest)
            return smallest
        smallest = self.next
        self.next += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.next and num not in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)
