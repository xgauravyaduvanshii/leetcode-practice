# LeetCode 2712. Minimum Cost to Make All Characters Equal — Medium
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
# Submission 2205207144 — Accepted, Python3
#
# My thinking: only the boundaries between unequal neighbours
# matter. A boundary between i and i+1 must be crossed by at
# least one flip, and the cheapest flip crossing it is either
# the prefix ending at i (cost i+1) or the suffix starting at
# i+1 (cost n-i-1). Adding the cheapest crossing cost at every
# unequal boundary is both necessary and sufficient.
class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        return sum(min(i + 1, n - i - 1) for i in range(n - 1) if s[i] != s[i + 1])
