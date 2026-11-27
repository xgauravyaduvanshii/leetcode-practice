# LeetCode 2039. The Time When the Network Becomes Idle — Medium
# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/
# Submission 2204375586 — Accepted, Python3
#
# My thinking: a message from server i takes 2 * dist[i] seconds for
# the round trip, where dist is the BFS distance from server 0. While
# waiting, the server resends every patience[i] seconds, so its last
# resend happens at ((2*dist[i] - 1) // patience[i]) * patience[i],
# and that message's reply arrives one second after the round trip.
# The network is idle when the latest such reply arrives, so I take
# the maximum over all servers except 0.
from collections import deque

class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        dist = [-1] * n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        ans = 0
        for i in range(1, n):
            d = 2 * dist[i]
            last = ((d - 1) // patience[i]) * patience[i]
            ans = max(ans, last + d + 1)
        return ans
