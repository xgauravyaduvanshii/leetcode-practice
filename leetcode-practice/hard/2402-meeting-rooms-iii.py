# LeetCode 2402. Meeting Rooms III — Hard
# https://leetcode.com/problems/meeting-rooms-iii/
# Submission 2201720265 — Accepted, Python3
#
# My thinking: a meeting takes the lowest
# free room, and if none is free it waits
# for the room that frees up first — two
# heaps keep the free rooms and the busy
# ones, and the room that hosts the most
# meetings wins.

import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        busy = []
        counts = [0] * n
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                free_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (free_time + end - start, room))
            counts[room] += 1
        return counts.index(max(counts))
