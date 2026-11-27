# LeetCode 1396. Design Underground System — Medium
# https://leetcode.com/problems/design-underground-system/
# Submission 2199048876 — Accepted, Python3
#
# My thinking: I remember each passenger's
# check-in station and time, and when they
# check out I add the trip time to that
# station pair's running total and count. The
# average is then one division.

from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}
        self.trips = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        total, count = self.trips[(start_station, stationName)]
        self.trips[(start_station, stationName)] = [total + t - start_time, count + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trips[(startStation, endStation)]
        return total / count
