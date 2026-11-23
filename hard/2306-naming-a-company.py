# LeetCode 2306. Naming a Company — Hard
# https://leetcode.com/problems/naming-a-company/
# Submission 2201671648 — Accepted, Python3
#
# My thinking: two names only pair up when
# swapping their first letters makes fresh
# names, so I group the tails by their
# first letter and count the tails each
# group has that the other one lacks.

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        groups = {}
        for idea in ideas:
            groups.setdefault(idea[0], set()).add(idea[1:])
        ans = 0
        letters = list(groups.keys())
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                a = groups[letters[i]]
                b = groups[letters[j]]
                common = len(a & b)
                ans += (len(a) - common) * (len(b) - common) * 2
        return ans
