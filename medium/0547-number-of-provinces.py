# LeetCode 547. Number of Provinces — Medium
# https://leetcode.com/problems/number-of-provinces/
# Submission 2198861181 — Accepted, Python3
#
# My thinking: connected cities form one province.
# I walk each unvisited city and flood through
# every city directly connected to it, counting one
# province per flood.

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        provinces = 0
        for city in range(n):
            if city in seen:
                continue
            provinces += 1
            stack = [city]
            seen.add(city)
            while stack:
                current = stack.pop()
                for neighbour in range(n):
                    if isConnected[current][neighbour] == 1 and neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
        return provinces
