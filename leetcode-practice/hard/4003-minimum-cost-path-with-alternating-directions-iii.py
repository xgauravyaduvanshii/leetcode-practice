# LeetCode 4003. Minimum Cost Path with Alternating Directions III — Hard
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/
# Submission 2203504749 — Accepted, Python3
import heapq
from typing import List


class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        # My thinking: the only thing that matters besides
        # the cell is the parity of the next action — odd
        # actions move right or down for free, even actions
        # move left or up for free, and every action flips
        # the parity. So Dijkstra over states (i, j, p):
        # from a state you may wait, paying penalty[i][j],
        # or step to a neighbour, paying its entrance cost
        # (i+1)*(j+1) plus penalty[i][j] when the step
        # breaks the parity rule. All costs are
        # non-negative, the start state costs the entrance
        # of (0, 0), and the first time the target is
        # popped from the heap its cost is minimal.
        INF = float("inf")
        dist = [[[INF, INF] for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 1
        pq = [(1, 0, 0, 0)]
        while pq:
            d, i, j, p = heapq.heappop(pq)
            if d != dist[i][j][p]:
                continue
            if i == m - 1 and j == n - 1:
                return d
            nd = d + penalty[i][j]
            if nd < dist[i][j][1 - p]:
                dist[i][j][1 - p] = nd
                heapq.heappush(pq, (nd, i, j, 1 - p))
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                free = (p == 0 and (di > 0 or dj > 0)) or (p == 1 and (di < 0 or dj < 0))
                nd = d + (ni + 1) * (nj + 1) + (0 if free else penalty[i][j])
                if nd < dist[ni][nj][1 - p]:
                    dist[ni][nj][1 - p] = nd
                    heapq.heappush(pq, (nd, ni, nj, 1 - p))
        return min(dist[m - 1][n - 1])
