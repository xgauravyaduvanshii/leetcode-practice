# LeetCode 2923. Find Champion I — Easy
# https://leetcode.com/problems/find-champion-i/
# Submission 2198696386 — Accepted, Python3
#
# My thinking: the champion beats every other team,
# so its row is all ones — the row with the most
# wins. I take the team whose row sums to the most.

from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return max(range(len(grid)), key=lambda i: sum(grid[i]))
