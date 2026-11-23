# LeetCode 2532. Time to Cross a Bridge — Hard
# https://leetcode.com/problems/time-to-cross-a-bridge/
# Submission 2201802291 — Accepted, Python3
#
# My thinking: the bridge is the only
# bottleneck, so I run the clock forward
# event by event — workers waiting to
# cross are ordered by how slow they are,
# the right side always goes first, and
# nobody new leaves the left once every
# box already has a carrier. A box counts
# as home the moment its carrier steps
# off the bridge on the left — the
# putting down after that does not add
# to the answer.

import heapq


class Solution:
    def findCrossingTime(self, n: int, k: int, time: list[list[int]]) -> int:
        # efficiency key: larger (left+right, index) = less efficient = higher priority
        def key(i):
            return (time[i][0] + time[i][2], i)

        wait_left = [(-key(i)[0], -key(i)[1], i) for i in range(k)]
        heapq.heapify(wait_left)
        wait_right = []
        picking = []  # (finish, worker)
        putting = []  # (finish, worker)
        crossing_left = []  # (finish, worker) — workers on the bridge, right to left
        sent = 0
        arrived = 0
        now = 0
        bridge_free = 0
        while True:
            # release finished pickers and putters into the waiting lines
            while picking and picking[0][0] <= now:
                _, w = heapq.heappop(picking)
                heapq.heappush(wait_right, (-key(w)[0], -key(w)[1], w))
            while putting and putting[0][0] <= now:
                _, w = heapq.heappop(putting)
                heapq.heappush(wait_left, (-key(w)[0], -key(w)[1], w))
            # a worker finishing the leftward crossing delivers a box
            while crossing_left and crossing_left[0][0] <= now:
                finish, w = heapq.heappop(crossing_left)
                arrived += 1
                if arrived == n:
                    return finish
                heapq.heappush(putting, (finish + time[w][3], w))
            if now >= bridge_free:
                if wait_right:
                    _, _, w = heapq.heappop(wait_right)
                    bridge_free = now + time[w][2]
                    heapq.heappush(crossing_left, (bridge_free, w))
                elif wait_left and sent < n:
                    _, _, w = heapq.heappop(wait_left)
                    bridge_free = now + time[w][0]
                    heapq.heappush(picking, (bridge_free + time[w][1], w))
                    sent += 1
                else:
                    # nobody can cross: jump to the next event strictly after now
                    cands = []
                    if picking:
                        cands.append(picking[0][0])
                    if putting:
                        cands.append(putting[0][0])
                    if crossing_left:
                        cands.append(crossing_left[0][0])
                    now = min(cands)
            else:
                # bridge busy: jump to the next event strictly after now
                cands = [bridge_free]
                if picking:
                    cands.append(picking[0][0])
                if putting:
                    cands.append(putting[0][0])
                if crossing_left:
                    cands.append(crossing_left[0][0])
                now = min(cands)
