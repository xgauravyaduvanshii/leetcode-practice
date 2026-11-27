# LeetCode 2285. Maximum Total Importance of Roads — Medium
# https://leetcode.com/problems/maximum-total-importance-of-roads/
# Submission 2204640809 — Accepted, Python3
#
# My thinking: a city's value is multiplied by its degree, so the cities
# with the most roads should get the biggest values. Count each city's
# degree, sort the degrees ascending, and hand out the values 1..n in
# the same ascending order — the rearrangement inequality says this
# pairing gives the largest possible total.
class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        deg = [0] * n
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
        deg.sort()
        ans = 0
        for i, d in enumerate(deg):
            ans += d * (i + 1)
        return ans
