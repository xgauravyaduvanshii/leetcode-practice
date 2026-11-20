# LeetCode 1722. Minimize Hamming Distance After Swap Operations — Medium
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
# Submission 2199921040 — Accepted, Python3
#
# My thinking: swaps only move values inside
# their connected group. I group the indices
# with union-find, then in each group I match
# as many target values as the source values
# allow.

from collections import Counter, defaultdict
from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in allowedSwaps:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)
        distance = 0
        for indices in groups.values():
            counts = Counter(source[i] for i in indices)
            for i in indices:
                if counts[target[i]] > 0:
                    counts[target[i]] -= 1
                else:
                    distance += 1
        return distance
