# LeetCode 4027. Elevator Requests III — Hard
# https://leetcode.com/problems/elevator-requests-iii/
# Submission 2203517162 — Accepted, Python3
from typing import List


class Solution:
    def minTime(self, n: int, start: int, requests: List[List[int]]) -> int:
        # My thinking: with at most 16 requests, try every
        # order they can be fulfilled in — a bitmask DP over
        # the set of requests done so far. dp[mask][i] is the
        # earliest time at which exactly the requests in mask
        # are fulfilled and the elevator stands at request
        # i's floor. Going from i to a new request j costs
        # the floor distance, and the elevator may have to
        # wait at j's floor until j's arrival time, so the
        # new time is max(old + |floor_i - floor_j|,
        # arrival_j). Starting out, reaching request i costs
        # max(|start - floor_i|, arrival_i). Passing through
        # a floor on the way to another request never beats
        # visiting it in order, so the cheapest order the DP
        # finds is the true optimum. The answer is the best
        # dp value over all last requests in the full mask.
        m = len(requests)
        floors = [r[1] for r in requests]
        arrive = [r[0] for r in requests]
        INF = float("inf")
        size = 1 << m
        dp = [[INF] * m for _ in range(size)]
        for i in range(m):
            dp[1 << i][i] = max(abs(start - floors[i]), arrive[i])
        for mask in range(size):
            for i in range(m):
                if not (mask >> i) & 1:
                    continue
                cur = dp[mask][i]
                if cur == INF:
                    continue
                for j in range(m):
                    if (mask >> j) & 1:
                        continue
                    t = cur + abs(floors[i] - floors[j])
                    if t < arrive[j]:
                        t = arrive[j]
                    nm = mask | (1 << j)
                    if t < dp[nm][j]:
                        dp[nm][j] = t
        return min(dp[size - 1])
