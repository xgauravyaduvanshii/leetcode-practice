# LeetCode 1976. Number of Ways to Arrive at Destination — Medium
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
# Submission 2204088264 — Accepted, Python3
#
# My thinking:
# This is a shortest-path counting problem, so Dijkstra's algorithm
# finds the shortest travel time from intersection 0 to every other
# intersection. Along the way I also keep, for each intersection, how
# many different shortest routes reach it.
# When I relax an edge and find a strictly shorter time to a neighbour,
# that neighbour's shortest time becomes the new time and its count
# resets to the count of the node I came from — every shortest route to
# the neighbour must now go through that node.
# When I relax an edge and find a time exactly equal to the neighbour's
# current shortest time, I have found more shortest routes, so I add
# the count of the node I came from to the neighbour's count.
# A longer time is ignored, since it can never be part of a shortest
# route. All counts are taken modulo 1_000_000_007, and the answer is
# the count stored for intersection n - 1.

import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]  # (travel time so far, intersection)
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for neighbour, travel in graph[node]:
                new_time = time + travel
                if new_time < dist[neighbour]:
                    dist[neighbour] = new_time
                    ways[neighbour] = ways[node]
                    heapq.heappush(heap, (new_time, neighbour))
                elif new_time == dist[neighbour]:
                    ways[neighbour] = (ways[neighbour] + ways[node]) % MOD

        return ways[n - 1] % MOD


if __name__ == "__main__":
    s = Solution()
    # Example 1: shortest time is 7, with 4 ways to arrive.
    assert s.countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
                            [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                            [0, 4, 5], [4, 6, 2]]) == 4
    # Example 2: only one road, so one way.
    assert s.countPaths(2, [[1, 0, 10]]) == 1
    # Edge case: a single intersection, already at the destination.
    assert s.countPaths(1, []) == 1
    print("All samples pass.")
