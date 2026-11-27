# LeetCode 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance — Medium
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# Submission 2199033200 — Accepted, Python3
#
# My thinking: Floyd-Warshall fills in the
# shortest distance between every pair of
# cities. The city with the fewest neighbours
# within the threshold wins, and ties go to the
# larger city number.

from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for a, b, w in edges:
            dist[a][b] = dist[b][a] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        best_city = -1
        best_count = n + 1
        for i in range(n):
            count = sum(1 for d in dist[i] if d <= distanceThreshold)
            if count <= best_count:
                best_count = count
                best_city = i
        return best_city
