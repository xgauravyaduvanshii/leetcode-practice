# LeetCode 2374. Node With Highest Edge Score — Medium
# https://leetcode.com/problems/node-with-highest-edge-score/
# Submission 2204764326 — Accepted, Python3
#
# My thinking: the edge score of a node is the sum of the indices of
# the edges pointing at it. One pass accumulates every edge's index
# into its target node's score, then I pick the smallest index whose
# score is largest (scanning in order and keeping only strictly larger
# scores gives the tie-break for free).
class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        n = len(edges)
        score = [0] * n
        for i, v in enumerate(edges):
            score[v] += i
        best = 0
        for i in range(1, n):
            if score[i] > score[best]:
                best = i
        return best
