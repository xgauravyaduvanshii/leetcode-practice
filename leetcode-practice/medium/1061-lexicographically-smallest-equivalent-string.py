# LeetCode 1061. Lexicographically Smallest Equivalent String — Medium
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Submission 2198996352 — Accepted, Python3
#
# My thinking: letters that must be equal form
# groups, and each group is named by its
# smallest letter. I merge the groups from the
# two strings, always pointing the bigger root
# at the smaller one.

from typing import List


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in zip(s1, s2):
            ra, rb = find(ord(a) - 97), find(ord(b) - 97)
            if ra != rb:
                if ra < rb:
                    parent[rb] = ra
                else:
                    parent[ra] = rb
        return "".join(chr(find(ord(ch) - 97) + 97) for ch in baseStr)
