# LeetCode 839. Similar String Groups — Hard
# https://leetcode.com/problems/similar-string-groups/
# Submission 2198681270 — Accepted, Python3
#
# My thinking: two strings are similar when they
# differ in at most two positions. I join every
# similar pair with union-find, and the number of
# groups left at the end is the answer.

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = list(range(len(strs)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def similar(a, b):
            diffs = 0
            for x, y in zip(a, b):
                if x != y:
                    diffs += 1
                    if diffs > 2:
                        return False
            return True

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if similar(strs[i], strs[j]):
                    parent[find(i)] = find(j)
        return len({find(i) for i in range(len(strs))})
