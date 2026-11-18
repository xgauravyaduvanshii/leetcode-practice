# LeetCode 1042. Flower Planting With No Adjacent — Medium
# https://leetcode.com/problems/flower-planting-with-no-adjacent/
# Submission 2198992800 — Accepted, Python3
#
# My thinking: each garden has at most three
# neighbours, so with four flower types there is
# always one free. I walk the gardens in order
# and give each the first colour none of its
# neighbours uses.

from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in paths:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        flowers = [0] * n
        for garden in range(n):
            used = {flowers[neighbour] for neighbour in graph[garden]}
            for colour in range(1, 5):
                if colour not in used:
                    flowers[garden] = colour
                    break
        return flowers
