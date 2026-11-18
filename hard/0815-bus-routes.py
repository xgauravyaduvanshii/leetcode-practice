# LeetCode 815. Bus Routes — Hard
# https://leetcode.com/problems/bus-routes/
# Submission 2198678487 — Accepted, Python3
#
# My thinking: I think in buses, not stops. From a
# stop I can board every bus that passes through it,
# and each boarding costs one. A breadth-first search
# over stops, remembering which buses I have already
# ridden, finds the fewest buses to the target.

from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].add(bus)
        seen_buses = set()
        queue = deque([(source, 0)])
        seen_stops = {source}
        while queue:
            stop, buses = queue.popleft()
            for bus in stop_to_buses[stop]:
                if bus in seen_buses:
                    continue
                seen_buses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1
                    if next_stop not in seen_stops:
                        seen_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))
        return -1
