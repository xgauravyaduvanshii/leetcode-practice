import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        # My thinking: drive as far as the tank allows, and whenever
        # it runs dry, take the biggest fuel stop I already passed —
        # that greedy choice keeps the stop count minimal.
        max_heap = []
        stops = 0
        fuel = startFuel
        prev = 0
        stations = stations + [[target, 0]]
        for position, gas in stations:
            fuel -= position - prev
            while fuel < 0 and max_heap:
                fuel += -heapq.heappop(max_heap)
                stops += 1
            if fuel < 0:
                return -1
            heapq.heappush(max_heap, -gas)
            prev = position
        return stops
