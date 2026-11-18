# LeetCode 295. Find Median from Data Stream — Hard
# https://leetcode.com/problems/find-median-from-data-stream/
# Submission 2198399869 — Accepted, Python3
#
# My thinking: I split the numbers into a lower
# half and an upper half. The lower half is a
# max-heap and the upper half a min-heap, so the
# biggest of the lower half and the smallest of the
# upper half sit next to each other in the middle.
# Each new number goes into the lower half first,
# then the halves are rebalanced so the lower half
# is never smaller. The median is the top of the
# lower half, or the average of the two tops when
# the halves are even.

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
