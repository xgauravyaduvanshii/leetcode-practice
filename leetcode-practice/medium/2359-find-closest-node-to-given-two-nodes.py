# LeetCode 2359. Find Closest Node to Given Two Nodes — Medium
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
# Submission 2204740972 — Accepted, Python3
#
# My thinking: each node has at most one outgoing edge, so walking from a
# start node traces a single chain (stopping at -1 or a repeat). I record
# the distance from node1 to every node on its chain, and the same from
# node2. The answer is the node on both chains that minimises the larger
# of the two distances, scanning in increasing node order so the smallest
# index wins ties.
class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def distances(start):
            dist = {}
            d = 0
            u = start
            while u != -1 and u not in dist:
                dist[u] = d
                d += 1
                u = edges[u]
            return dist
        d1 = distances(node1)
        d2 = distances(node2)
        ans = -1
        best = float('inf')
        for v in range(len(edges)):
            if v in d1 and v in d2:
                m = max(d1[v], d2[v])
                if m < best:
                    best = m
                    ans = v
        return ans
