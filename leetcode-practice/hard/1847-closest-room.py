# LeetCode 1847. Closest Room — Hard
# https://leetcode.com/problems/closest-room/
# Submission 2201197491 — Accepted, Python3
#
# My thinking: I sort the rooms and the queries
# by size, then sweep the queries from biggest to
# smallest, keeping the room ids that qualify in
# a sorted list and taking the id nearest to the
# preferred one.

import bisect

class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        rooms.sort(key=lambda r: -r[1])
        order = sorted(range(len(queries)), key=lambda i: -queries[i][1])
        ids = []
        ans = [-1] * len(queries)
        j = 0
        for qi in order:
            pref, min_size = queries[qi]
            while j < len(rooms) and rooms[j][1] >= min_size:
                bisect.insort(ids, rooms[j][0])
                j += 1
            if not ids:
                ans[qi] = -1
                continue
            pos = bisect.bisect_left(ids, pref)
            best = -1
            if pos < len(ids):
                best = ids[pos]
            if pos > 0:
                cand = ids[pos - 1]
                if best == -1 or pref - cand <= best - pref:
                    best = cand
            ans[qi] = best
        return ans
