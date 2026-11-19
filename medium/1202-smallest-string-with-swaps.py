# LeetCode 1202. Smallest String With Swaps — Medium
# https://leetcode.com/problems/smallest-string-with-swaps/
# Submission 2199012210 — Accepted, Python3
#
# My thinking: positions linked by swaps can
# trade letters freely. I group the linked
# positions, then put each group's letters
# back in sorted order at its smallest spots.

from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in pairs:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        groups = defaultdict(list)
        for i, ch in enumerate(s):
            groups[find(i)].append(i)
        result = list(s)
        for indices in groups.values():
            letters = sorted(s[i] for i in indices)
            for i, ch in zip(sorted(indices), letters):
                result[i] = ch
        return "".join(result)
