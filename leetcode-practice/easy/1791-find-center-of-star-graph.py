# LeetCode 1791. Find Center of Star Graph — Easy
# https://leetcode.com/problems/find-center-of-star-graph/
# Submission 2197598231 — Accepted, Python3
#
# My thinking: the center of a star graph is in
# every edge. So I look at the first two edges —
# the number they have in common is the center.

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
