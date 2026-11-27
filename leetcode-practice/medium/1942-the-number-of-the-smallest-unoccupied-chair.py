# LeetCode 1942. The Number of the Smallest Unoccupied Chair — Medium
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
# Submission 2201732157 — Accepted, Python3
#
# My thinking: friends arrive in order and
# take the smallest free chair — I keep
# the busy chairs in one heap by leaving
# time and the free chairs in another by
# number, and hand the target friend
# whichever chair is smallest when they
# walk in.

import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key=lambda i: times[i][0])
        busy = []
        free = []
        next_chair = 0
        for i in order:
            arrival, leaving = times[i]
            while busy and busy[0][0] <= arrival:
                _, chair = heapq.heappop(busy)
                heapq.heappush(free, chair)
            if free:
                chair = heapq.heappop(free)
            else:
                chair = next_chair
                next_chair += 1
            if i == targetFriend:
                return chair
            heapq.heappush(busy, (leaving, chair))
        return -1
