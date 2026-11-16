# LeetCode 1184. Distance Between Bus Stops — Easy
# https://leetcode.com/problems/distance-between-bus-stops/
# Submission 2197561049 — Accepted, Python3
#
# My thinking: there are two ways round the circle —
# clockwise and the other way. I add up the
# clockwise distance between the two stops, and the
# other way is just the total minus that. The
# shorter of the two is the answer.

class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        return min(clockwise, sum(distance) - clockwise)
