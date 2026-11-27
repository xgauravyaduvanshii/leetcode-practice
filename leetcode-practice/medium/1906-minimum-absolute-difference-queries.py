# LeetCode 1906. Minimum Absolute Difference Queries — Medium
# https://leetcode.com/problems/minimum-absolute-difference-queries/
# Submission 2201268295 — Accepted, Python3
#
# My thinking: the values only run from 1 to 100,
# so I keep a prefix count per value and answer
# each query by walking the values in order and
# keeping the smallest gap between two that
# actually show up.

class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        pref = [[0] * 101]
        for x in nums:
            row = pref[-1][:]
            row[x] += 1
            pref.append(row)
        ans = []
        for l, r in queries:
            prev = -1
            best = -1
            for v in range(1, 101):
                if pref[r + 1][v] - pref[l][v] > 0:
                    if prev != -1:
                        d = v - prev
                        if best == -1 or d < best:
                            best = d
                    prev = v
            ans.append(best)
        return ans
